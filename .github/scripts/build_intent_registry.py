#!/usr/bin/env python3
"""Build and validate the deterministic Playbook/Skill intent registry."""
import argparse
from collections import Counter
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "Catalog" / "INTENT-REGISTRY.json"
ROUTING_SOURCE = ROOT / ".github" / "intent-routing.json"
DEFAULT_PRIORITY = {"playbook": 100, "skill": 50}
FALLBACK_PLAYBOOK = "PLAY-0006"
MAX_SKILLS = 2
MAX_EXTRA_TOKENS = 5


class RegistryError(ValueError):
    pass


def normalize(value):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", str(value).lower())).strip()


def _string_list(value, field, asset_id):
    if value in (None, ""):
        return []
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise RegistryError(f"{asset_id}: {field} must be a string list")
    return value


def load_routing_contract(path=ROUTING_SOURCE):
    data = json.loads(path.read_text())
    if data.get("schema_version") != 1 or not isinstance(data.get("assets"), dict):
        raise RegistryError(".github/intent-routing.json has an unsupported schema")
    return data["assets"]


def build_registry(entries, routing_contract, root=ROOT):
    assets = []
    seen = {}
    current_ids = {
        asset_id
        for asset_id, entry in entries.items()
        if entry.get("folder") in {"Playbooks", "Skills"}
        and str(entry.get("fm", {}).get("status") or "").strip() == "current"
    }
    configured_ids = set(routing_contract)
    missing = sorted(current_ids - configured_ids)
    extra = sorted(configured_ids - current_ids)
    if missing or extra:
        raise RegistryError(
            f"routing contract coverage mismatch; missing={missing or 'none'}; extra={extra or 'none'}"
        )
    for asset_id in sorted(entries):
        entry = entries[asset_id]
        if entry.get("folder") not in {"Playbooks", "Skills"}:
            continue
        fm = entry.get("fm", {})
        kind = fm.get("type")
        if kind not in DEFAULT_PRIORITY:
            raise RegistryError(f"{asset_id}: type must be playbook or skill")
        title = str(fm.get("title") or "").strip()
        if not title:
            raise RegistryError(f"{asset_id}: title is required for intent routing")
        status = str(fm.get("status") or "").strip()
        route = routing_contract.get(asset_id, {})
        curated = _string_list(route.get("triggers"), "contract triggers", asset_id)
        if status == "current" and not curated:
            raise RegistryError(f"{asset_id}: current asset requires curated contract triggers")
        raw_triggers = (
            [title]
            + _string_list(fm.get("trigger_phrases"), "trigger_phrases", asset_id)
            + curated
        )
        triggers = sorted({normalize(item) for item in raw_triggers if normalize(item)})
        if not triggers:
            raise RegistryError(f"{asset_id}: at least one trigger is required")
        exclusions = sorted({
            normalize(item)
            for item in _string_list(route.get("exclusions"), "contract exclusions", asset_id)
            if normalize(item)
        })
        if status == "current" and "exclusions" not in route:
            raise RegistryError(f"{asset_id}: contract exclusions are required")
        if status == "current" and "priority" not in route:
            raise RegistryError(f"{asset_id}: contract priority is required")
        priority = route.get("priority", DEFAULT_PRIORITY[kind])
        if isinstance(priority, str) and re.fullmatch(r"-?\d+", priority):
            priority = int(priority)
        if not isinstance(priority, int) or isinstance(priority, bool):
            raise RegistryError(f"{asset_id}: routing_priority must be an integer")
        path = str(Path(entry["path"]).relative_to(root)).replace("\\", "/")
        asset = {
            "id": asset_id,
            "type": kind,
            "title": title,
            "status": status,
            "priority": priority,
            "triggers": triggers,
            "exclusions": exclusions,
            "path": path,
        }
        assets.append(asset)
        if status == "current":
            for trigger in triggers:
                key = (kind, trigger)
                seen.setdefault(key, []).append(asset_id)

    duplicates = [
        f"duplicate current trigger '{trigger}' for {kind} is shared by {', '.join(ids)}"
        for (kind, trigger), ids in sorted(seen.items())
        if len(set(ids)) > 1
    ]
    if duplicates:
        raise RegistryError("; ".join(duplicates))
    if not any(asset["id"] == FALLBACK_PLAYBOOK and asset["status"] == "current" for asset in assets):
        raise RegistryError(f"current fallback {FALLBACK_PLAYBOOK} is missing")
    return {
        "schema_version": 1,
        "generated": True,
        "source": ".github/intent-routing.json plus Playbook and Skill frontmatter",
        "routing": {
            "fallback_playbook": FALLBACK_PLAYBOOK,
            "max_skills": MAX_SKILLS,
            "rule": "Match normalized whole phrases; select the unique highest-ranked playbook and up to two skills; surface score ties; use fallback only when no playbook matches.",
        },
        "assets": assets,
    }


def _phrase_match(text, phrase):
    """Match all trigger tokens inside a small, order-independent word window."""
    words = text.split()
    required = phrase.split()
    if not required:
        return False
    need = Counter(required)
    have = Counter()
    covered = 0
    left = 0
    for right, word in enumerate(words):
        have[word] += 1
        if have[word] <= need[word]:
            covered += 1
        while covered == len(required):
            if right - left + 1 <= len(required) + MAX_EXTRA_TOKENS:
                return True
            left_word = words[left]
            if have[left_word] <= need[left_word]:
                covered -= 1
            have[left_word] -= 1
            left += 1
    return False


def _ranked_matches(registry, utterance, kind):
    text = normalize(utterance)
    matches = []
    for asset in registry.get("assets", []):
        if asset.get("type") != kind or asset.get("status") != "current":
            continue
        if any(_phrase_match(text, phrase) for phrase in asset.get("exclusions", [])):
            continue
        matched = [phrase for phrase in asset.get("triggers", []) if _phrase_match(text, phrase)]
        if not matched:
            continue
        best = max(matched, key=lambda phrase: (len(phrase.split()), len(phrase)))
        score = (asset["priority"], len(best.split()), len(best))
        matches.append({"id": asset["id"], "score": score, "trigger": best})
    return sorted(matches, key=lambda row: (row["score"], row["id"]), reverse=True)


def route_intent(registry, utterance):
    playbooks = _ranked_matches(registry, utterance, "playbook")
    ambiguous_playbooks = []
    if not playbooks:
        playbook = registry["routing"]["fallback_playbook"]
    elif len(playbooks) > 1 and playbooks[0]["score"] == playbooks[1]["score"]:
        playbook = None
        ambiguous_playbooks = [row["id"] for row in playbooks if row["score"] == playbooks[0]["score"]]
    else:
        playbook = playbooks[0]["id"]

    skills = _ranked_matches(registry, utterance, "skill")
    limit = int(registry["routing"].get("max_skills", MAX_SKILLS))
    selected_skills = [row["id"] for row in skills[:limit]]
    ambiguous_skills = []
    if len(skills) > limit and skills[limit - 1]["score"] == skills[limit]["score"]:
        cutoff = skills[limit - 1]["score"]
        ambiguous_skills = [row["id"] for row in skills if row["score"] == cutoff]
        selected_skills = [row["id"] for row in skills if row["score"] > cutoff]
    return {
        "playbook": playbook,
        "skills": selected_skills,
        "ambiguous_playbooks": ambiguous_playbooks,
        "ambiguous_skills": ambiguous_skills,
    }


def simulate_routes(registry, fixture):
    if fixture.get("schema_version") != 1:
        raise RegistryError("routing fixture has an unsupported schema")
    cases = fixture.get("cases")
    minimum = fixture.get("minimum_cases")
    if not isinstance(cases, list) or not cases:
        raise RegistryError("routing fixture requires non-empty cases")
    if not isinstance(minimum, int) or isinstance(minimum, bool) or minimum < 1:
        raise RegistryError("routing fixture requires a positive minimum_cases")
    if len(cases) < minimum:
        raise RegistryError(f"routing fixture has {len(cases)} cases; minimum is {minimum}")
    names = [case.get("name") for case in cases]
    if any(not isinstance(name, str) or not name.strip() for name in names):
        raise RegistryError("every routing case requires a non-empty name")
    if len(set(names)) != len(names):
        raise RegistryError("routing fixture case names must be unique")

    current_playbooks = {
        asset["id"] for asset in registry["assets"]
        if asset["status"] == "current" and asset["type"] == "playbook"
    }
    current_skills = {
        asset["id"] for asset in registry["assets"]
        if asset["status"] == "current" and asset["type"] == "skill"
    }
    covered_playbooks = {
        asset_id
        for case in cases
        for asset_id in ([case.get("playbook")] + case.get("ambiguous_playbooks", []))
        if asset_id
    }
    covered_skills = {
        asset_id
        for case in cases
        for asset_id in (
            case.get("skills", [])
            + case.get("required_skills", [])
            + case.get("excluded_skills", [])
        )
    }
    if fixture.get("coverage") != {"playbooks": "all_current", "skills": "all_current"}:
        raise RegistryError("routing fixture must require all-current Playbook and Skill coverage")
    if covered_playbooks != current_playbooks or covered_skills != current_skills:
        raise RegistryError(
            "routing fixture coverage mismatch; "
            f"playbooks missing={sorted(current_playbooks - covered_playbooks)} "
            f"extra={sorted(covered_playbooks - current_playbooks)}; "
            f"skills missing={sorted(current_skills - covered_skills)} "
            f"extra={sorted(covered_skills - current_skills)}"
        )

    failures = []
    for case in cases:
        if not isinstance(case.get("utterance"), str) or not case["utterance"].strip():
            failures.append(f"{case.get('name')}: utterance is required")
            continue
        result = route_intent(registry, case.get("utterance", ""))
        name = case.get("name", "unnamed")
        if result["playbook"] != case.get("playbook"):
            failures.append(f"{name}: playbook {result['playbook']} != {case.get('playbook')}")
        if "skills" in case and result["skills"] != case["skills"]:
            failures.append(f"{name}: skills {result['skills']} != {case['skills']}")
        required = set(case.get("required_skills", []))
        if not required.issubset(result["skills"]):
            failures.append(f"{name}: missing required skills {sorted(required - set(result['skills']))}")
        excluded = set(case.get("excluded_skills", []))
        if excluded.intersection(result["skills"]):
            failures.append(f"{name}: excluded skills selected {sorted(excluded.intersection(result['skills']))}")
        expected_ambiguous = set(case.get("ambiguous_playbooks", []))
        if expected_ambiguous != set(result["ambiguous_playbooks"]):
            failures.append(
                f"{name}: ambiguous playbooks {result['ambiguous_playbooks']} "
                f"!= {sorted(expected_ambiguous)}"
            )
    if failures:
        raise RegistryError("; ".join(failures))
    return len(cases)


def collect_live_entries():
    sys.path.insert(0, str(ROOT / ".github" / "scripts"))
    from library_scan import collect_entries
    return collect_entries()


def render(registry):
    return json.dumps(registry, indent=2, sort_keys=True) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser()
    action = parser.add_mutually_exclusive_group()
    action.add_argument("--check", action="store_true")
    action.add_argument("--route")
    action.add_argument("--simulate", type=Path)
    args = parser.parse_args(argv)
    try:
        registry = build_registry(collect_live_entries(), load_routing_contract())
        rendered = render(registry)
        if args.check:
            if not OUTPUT.exists() or OUTPUT.read_text() != rendered:
                raise RegistryError("Catalog/INTENT-REGISTRY.json is stale; rebuild it")
            print("Intent registry is complete, unique, and current.")
            return 0
        if args.route is not None:
            print(json.dumps(route_intent(registry, args.route), indent=2, sort_keys=True))
            return 0
        if args.simulate is not None:
            count = simulate_routes(registry, json.loads(args.simulate.read_text()))
            print(f"Intent routing simulations passed: {count}/{count}.")
            return 0
        OUTPUT.write_text(rendered)
        print("Built Catalog/INTENT-REGISTRY.json.")
        return 0
    except (OSError, json.JSONDecodeError, RegistryError) as exc:
        print(f"INTENT REGISTRY FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
