#!/usr/bin/env python3
"""Prepare a detached, local scratch candidate; never publish or attest readiness.

The caller supplies a clean source snapshot and an origin containing main.
Fetching current main is read-only; no remote writes are performed. Generated files remain in the working tree. A private index measures the
fixed point without staging files in the caller's index or creating commits.
"""
import argparse
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / ".github/scripts"))


class PreparationError(ValueError):
    pass


class Runner:
    def __init__(self, root, evidence):
        self.root = root
        self.evidence = evidence
        self.env = os.environ.copy()
        self.env.pop("GIT_INDEX_FILE", None)
        self.env.pop("SESSION_PACK_SOURCE_BASE", None)
        # Candidate validation is defined over UTF-8 repository content. Make
        # every child Python process use that encoding instead of the host
        # locale (notably Windows cp1252), including nested test processes.
        self.env["PYTHONUTF8"] = "1"
        self.env["PYTHONIOENCODING"] = "utf-8"
        self.index_file = None
        self.source_base = None

    def run(self, command, allow_failure=False, env=None):
        print("+", " ".join(command), flush=True)
        proc = subprocess.run(command, cwd=self.root, env=self.env if env is None else env,
                              capture_output=True, text=True, encoding="utf-8")
        self.evidence["checks"].append({"command": command, "returncode": proc.returncode})
        if proc.stdout:
            print(proc.stdout, end="", flush=True)
        if proc.stderr:
            print(proc.stderr, end="", file=sys.stderr, flush=True)
        if proc.returncode and not allow_failure:
            raise PreparationError("command failed: " + " ".join(command))
        return proc

    def git(self, *args):
        env = self.env.copy()
        if self.index_file and (args[0] in {"read-tree", "add", "write-tree"} or
                                (args[0] == "diff" and "--cached" in args)):
            env["GIT_INDEX_FILE"] = self.index_file
        return self.run(["git", *args], env=env).stdout.strip()

    def script(self, name, *args, allow_failure=False):
        env = self.env.copy()
        if name == "validate_repo_state.py" and self.index_file:
            env["GIT_INDEX_FILE"] = self.index_file
        if name == "build_session_pack.py" and self.source_base:
            env["SESSION_PACK_SOURCE_BASE"] = self.source_base
        return self.run([sys.executable, ".github/scripts/" + name, *args], allow_failure, env)




def guard(runner, scratch, evidence_path, base_branch):
    if not scratch:
        raise PreparationError("--scratch-candidate is required; use an isolated local checkout")
    if runner.root == evidence_path or runner.root in evidence_path.parents:
        raise PreparationError("evidence must be outside the candidate checkout")
    if base_branch != "main":
        raise PreparationError("the governed candidate comparison base must be main")
    if Path(runner.git("rev-parse", "--show-toplevel")).resolve() != runner.root:
        raise PreparationError("script root must be the candidate repository root")
    if runner.run(["git", "symbolic-ref", "-q", "HEAD"], allow_failure=True).returncode != 1:
        raise PreparationError("candidate HEAD must be detached; no branch may be mutated")
    git_dir = Path(runner.git("rev-parse", "--absolute-git-dir")).resolve()
    if git_dir != runner.root / ".git" or (git_dir / "commondir").exists():
        raise PreparationError("use an independent scratch checkout, not a shared worktree")
    if runner.git("status", "--porcelain", "--untracked-files=all"):
        raise PreparationError("candidate must be a clean HEAD snapshot, including all source changes")
    if runner.git("config", "--get-all", "remote.origin.fetch") != "+refs/heads/*:refs/remotes/origin/*":
        raise PreparationError("origin must use the standard remote-tracking fetch refspec")
    runner.git("fetch", "origin", base_branch, "--depth=1000")
    runner.git("merge-base", "--is-ancestor", "origin/" + base_branch, "HEAD")
    return runner.git("rev-parse", "HEAD")


def prepare(runner, base_branch, source_sha, temp):
    """Compatibility entry point; all candidate work has one owner."""
    from final_candidate_checks import validate_candidate
    validate_candidate(runner, base_branch, source_sha, temp)




def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-branch", default="main")
    parser.add_argument("--scratch-candidate", action="store_true")
    parser.add_argument("--evidence", required=True, type=Path)
    args = parser.parse_args(argv)
    evidence_path = args.evidence.resolve()
    evidence = {"automation": "FAIL", "checks": [], "candidate_ready": False}
    runner = Runner(ROOT, evidence)
    try:
        source_sha = guard(runner, args.scratch_candidate, evidence_path, args.base_branch)
        runner.git("fetch", "origin", "staging")
        staging_before = runner.git("rev-parse", "origin/staging")
        with tempfile.TemporaryDirectory(prefix="library-prepare-") as directory:
            prepare(runner, args.base_branch, source_sha, Path(directory))
        runner.git("fetch", "origin", "main", "staging")
        if runner.git("rev-parse", "origin/main") != evidence["base_sha"]:
            raise PreparationError("main changed during preparation")
        if runner.git("rev-parse", "origin/staging") != staging_before:
            raise PreparationError("staging changed during preparation")
    except (PreparationError, OSError, ValueError) as exc:
        evidence.update(automation="FAIL", error=str(exc))
        print("PREPARATION FAIL: " + str(exc), file=sys.stderr)
    if args.scratch_candidate and evidence_path != ROOT and ROOT not in evidence_path.parents:
        evidence_path.write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    return 0 if evidence.get("automation") == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
