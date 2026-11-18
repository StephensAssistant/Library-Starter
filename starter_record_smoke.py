"""Exercise starter record creation in a disposable clone of a committed tree."""

import argparse
import datetime
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path


def run(root, *command, capture=False):
    result = subprocess.run(command, cwd=root, check=True, text=True, capture_output=capture)
    return result.stdout.strip() if capture else None


def write(root, path, text):
    target = root / path
    if target.exists():
        raise ValueError(f"Fixture would overwrite {path}")
    target.write_text(text, encoding="utf-8", newline="\n")


def python(root, *command, capture=False):
    return run(root, sys.executable, "-X", "utf8", *command, capture=capture)


def make_fixture(root, folder, prefix):
    today = datetime.date.today().isoformat()
    ids = python(root, ".github/scripts/allocate_ids.py", prefix,
                 "2" if prefix == "ART" else "1", "--requested-by", "starter-smoke", capture=True).split(",")
    text = (root / folder / "_TEMPLATE.md").read_text(encoding="utf-8")
    if prefix == "CHAT":
        text = text.replace("CHAT-<NNNN>", ids[0]).replace("<one-line summary>", "Starter smoke conversation")
        text = re.sub(r"^Links: .*", "Links: []", text, flags=re.MULTILINE)
        write(root, f"Chats/{today}.md", re.sub(r"<[^>]+>", "Fictional smoke evidence.", text))
        return
    header, frontmatter, body = text.split("---", 2)
    if header.strip():
        raise ValueError(f"Unexpected template layout for {folder}")
    native_id, record_id = (ids[0], ids[1]) if prefix == "ART" else (None, ids[0])
    fields = {
        "id": record_id, "title": "Fictional starter smoke " + folder,
        "created": today, "updated": today, "owner": "Library owner",
        "priority": "low", "effort": "quick", "work_class": "learning",
        "next_action": "Verify starter smoke path", "recorded_at": today,
        "source": "Fictional smoke input", "source_reference": "",
        "participants": ["Fictional participant"], "tags": ["starter-smoke"],
        "trigger_phrases": [f"Exercise fictional starter smoke {folder}"],
    }
    if native_id:
        fields["stored_at"] = f"Artifacts/{native_id}-starter-smoke.txt"
        write(root, fields["stored_at"], "Fictional artifact payload.\n")
    frontmatter = "\n".join(
        f"{name}: {json.dumps(fields[name], ensure_ascii=False)}"
        if name in fields else line
        for line in frontmatter.strip().splitlines()
        for name in [line.partition(":")[0]]
    )
    if prefix in {"PROJ", "TICK"}:
        plan_path = f"Planning/{record_id}.md"
        plan = (root / "Planning/_TEMPLATE.md").read_text(encoding="utf-8").replace("PARENT-ID", record_id)
        write(root, plan_path, re.sub(r"<[^>]+>", "Verify the fictional setup.", plan))
        body = re.sub(r"Planning/(?:PROJ|TICK|PARENT)-[^)\s]+\.md", plan_path, body)
        if plan_path not in body:
            body += f"\n\nLive plan: {plan_path}\n"
    body = re.sub(r"<[^>]+>", "Fictional setup evidence.", body)
    write(root, f"{folder}/{record_id}-starter-smoke.md", f"---\n{frontmatter}\n---{body}")


def smoke(source):
    # Test exactly the committed tree. Native files and reservations exist only in this clone.
    with tempfile.TemporaryDirectory(prefix="library-starter-smoke-") as temp:
        root = Path(temp) / "checkout"
        run(source, "git", "clone", "--no-local", str(source), str(root))
        config = json.loads((root / ".github/type-prefixes.json").read_text(encoding="utf-8"))
        python(root, ".github/scripts/validate_repo_state.py")
        for folder, prefix in (config["folders"] | config.get("shared_files", {})).items():
            if prefix == "FLOW":
                python(root, ".github/tests/test_workflows.py", "WorkflowTests.test_draft_is_valid_but_not_invocable", "-v")
                print("PASS FLOW draft contract (isolated upstream fixture)")
                continue
            make_fixture(root, folder, prefix)
            run(root, "git", "add", "--all")
            python(root, ".github/scripts/validate_repo_state.py")
            print(f"PASS {folder} ({prefix}) record path")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Committed starter repository")
    smoke(parser.parse_args().source.resolve())
