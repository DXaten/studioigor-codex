#!/usr/bin/env python3
"""Small, stdlib-only project journal for the Codex web-game skill."""

import argparse
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

PHASES = [
    "start", "idea", "style", "web stack", "playable prototype", "mechanics",
    "vertical slice", "content", "polish", "release", "complete",
]
DIR = ".studioigor"


def project_root(start):
    path = Path(start).expanduser().resolve()
    for candidate in (path, *path.parents):
        if (candidate / DIR / "state.json").exists():
            return candidate
    raise SystemExit(f"No {DIR}/state.json from {path}; run `studio.py init <folder> --name ...`.")


def save(root, state):
    dest = root / DIR / "state.json"
    dest.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def load(root):
    return json.loads((root / DIR / "state.json").read_text(encoding="utf-8"))


def journal(root, line):
    with (root / DIR / "JOURNAL.md").open("a", encoding="utf-8") as out:
        out.write(f"- {datetime.now(timezone.utc).isoformat(timespec='seconds')} — {line}\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    init = sub.add_parser("init", help="initialize a game project without overwriting files")
    init.add_argument("folder")
    init.add_argument("--name", required=True)
    for name in ("status", "phase", "reopen", "decide", "note"):
        p = sub.add_parser(name)
        p.add_argument("--root", default=".")
        if name == "phase":
            p.add_argument("number", type=int, choices=range(len(PHASES) - 1))
            p.add_argument("--evidence", required=True)
        elif name == "reopen":
            p.add_argument("number", type=int, choices=range(len(PHASES)))
        elif name == "decide":
            p.add_argument("decision")
            p.add_argument("--by", choices=("user", "agent"), required=True)
            p.add_argument("--why", required=True)
        elif name == "note":
            p.add_argument("done")
            p.add_argument("next")
    args = parser.parse_args()
    if args.command == "init":
        root = Path(args.folder).expanduser().resolve()
        root.mkdir(parents=True, exist_ok=True)
        folder = root / DIR
        folder.mkdir(exist_ok=True)
        state_file = folder / "state.json"
        if not state_file.exists():
            save(root, {"name": args.name, "phase": 0, "completed": {}, "last_note": None})
        for name, title in (
            ("CONCEPT.md", "Concept"), ("ART_BIBLE.md", "Art bible"),
            ("DESIGN.md", "Design and mechanics"), ("TECH.md", "Web stack"),
            ("ASSETS.md", "Assets and licenses"), ("PLAYTESTS.md", "Playtests"),
            ("RELEASE.md", "Release"), ("JOURNAL.md", "Journal"),
        ):
            target = folder / name
            if not target.exists():
                target.write_text(f"# {title}\n", encoding="utf-8")
        if not (root / "AGENTS.md").exists():
            template = Path(__file__).resolve().parent / "templates" / "AGENTS.md"
            (root / "AGENTS.md").write_text(
                template.read_text(encoding="utf-8").replace("{skill}", str(Path(__file__).resolve().parent.parent)),
                encoding="utf-8",
            )
        if subprocess.run(["git", "rev-parse", "--is-inside-work-tree"], cwd=root, capture_output=True).returncode:
            subprocess.run(["git", "init", "-b", "main"], cwd=root, check=True)
        print(f"Initialized {args.name}: {root}")
        return
    root = project_root(args.root)
    state = load(root)
    if args.command == "status":
        print(f"{state['name']} | phase {state['phase']}: {PHASES[state['phase']]} | {root}")
        for number, evidence in sorted(state["completed"].items(), key=lambda item: int(item[0])):
            print(f"  done {number}: {PHASES[int(number)]} — {evidence}")
        if state.get("last_note"):
            print(f"  next: {state['last_note']['next']}")
    elif args.command == "phase":
        if args.number != state["phase"]:
            raise SystemExit(f"Current phase is {state['phase']}; finish it before phase {args.number}.")
        state["completed"][str(args.number)] = args.evidence
        state["phase"] = args.number + 1
        save(root, state)
        journal(root, f"Phase {args.number} ({PHASES[args.number]}) complete: {args.evidence}")
        print(f"Now phase {state['phase']}: {PHASES[state['phase']]}")
    elif args.command == "reopen":
        if args.number > state["phase"]:
            raise SystemExit("Can only reopen the current or an earlier phase.")
        state["phase"] = args.number
        save(root, state)
        journal(root, f"Reopened phase {args.number}: {PHASES[args.number]}")
        print(f"Now phase {args.number}: {PHASES[args.number]}")
    elif args.command == "decide":
        journal(root, f"Decision ({args.by}): {args.decision}; reason: {args.why}")
    elif args.command == "note":
        state["last_note"] = {"done": args.done, "next": args.next}
        save(root, state)
        journal(root, f"Done: {args.done}; next: {args.next}")


if __name__ == "__main__":
    main()
