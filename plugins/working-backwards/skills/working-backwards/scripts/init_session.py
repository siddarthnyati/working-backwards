#!/usr/bin/env python3
"""Create a Working Backwards session directory.

Makes wb/<session-id>/, writes session.json with the chosen mode, and copies the
templates for the stages that mode actually runs — so the working directory shows
the shape of the session rather than every artifact the skill could ever produce.

Usage:
    python init_session.py <session-id> [--mode full|targeted|lightweight]
                           [--initiative "Short name"] [--root .] [--force]

Standard library only.
"""

import argparse
import datetime
import json
import os
import shutil
import sys

MODES = {
    "full": [0, 1, 2, 3, 4, 5, 6, 7, 8],
    "targeted": [0, 1, 2, 5, 6, 7],
    "lightweight": [0, 1, 2, 6],
}

# Stage -> template filenames. Stage 2 in targeted/lightweight is internal-only ("2i").
STAGE_TEMPLATES = {
    0: ["00-intake.md"],
    1: ["01-press-release.md"],
    2: ["02-faq-external.md", "02-faq-internal.md", "02-faq-regional.md"],
    3: ["03-demo-spec.md"],
    4: ["04-docs.md"],
    5: ["05-telemetry.md"],
    6: ["06-requirements.md"],
    7: ["07-release-plan.md"],
    8: ["08-readiness.md"],
}

ALWAYS = ["BLOCKERS.md", "DECISIONS.md", "QUESTIONS.md", "CONFIDENCE.md"]

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(SKILL_DIR, "assets", "templates")


def templates_for(mode):
    stages = MODES[mode]
    names = []
    for stage in stages:
        for name in STAGE_TEMPLATES[stage]:
            # Targeted and Lightweight run stage "2i" — the internal bank only.
            if stage == 2 and mode != "full" and not name.endswith("internal.md"):
                continue
            names.append(name)
    return names + ALWAYS


def build_session(session_id, mode, initiative, today):
    planned = MODES[mode]
    skipped = [s for s in MODES["full"] if s not in planned]
    return {
        "session_id": session_id,
        "created": today,
        "updated": today,
        "initiative": initiative or session_id,
        "mode": mode,
        "stages": {
            "planned": planned,
            "skipped": skipped,
            "current": 0,
            "completed": [],
        },
        "context": {
            "tier": 0,
            "path": "wb/context/",
            "files": [],
            "dimensions_not_evaluable": [4, 6],
        },
        "critic": {"verdicts": [], "overrides": []},
        "blockers": [],
        "questions": [],
        "claims": {"observed": 0, "reported": 0, "assumed": 0, "unknown": 0},
        "artifacts": {},
    }


def detect_context(root):
    """Report what's in wb/context/, if anything. Tier is stated, never assumed."""
    ctx = os.path.join(root, "wb", "context")
    if not os.path.isdir(ctx):
        return 0, []
    files = sorted(
        f for f in os.listdir(ctx) if not f.startswith(".") and os.path.isfile(os.path.join(ctx, f))
    )
    return (1 if files else 0), files


def main(argv=None):
    p = argparse.ArgumentParser(description="Create a Working Backwards session.")
    p.add_argument("session_id", help="short slug, e.g. ghost-seats")
    p.add_argument("--mode", choices=sorted(MODES), default="full")
    p.add_argument("--initiative", default=None, help="human-readable initiative name")
    p.add_argument("--root", default=".", help="repo root; wb/ is created under it")
    p.add_argument("--force", action="store_true", help="overwrite an existing session dir")
    args = p.parse_args(argv)

    session_dir = os.path.join(args.root, "wb", args.session_id)
    if os.path.exists(session_dir) and not args.force:
        print(
            "error: %s already exists. Resume it, or pass --force to overwrite." % session_dir,
            file=sys.stderr,
        )
        return 1
    os.makedirs(session_dir, exist_ok=True)

    today = datetime.date.today().isoformat()
    session = build_session(args.session_id, args.mode, args.initiative, today)

    tier, ctx_files = detect_context(args.root)
    session["context"]["tier"] = tier
    session["context"]["files"] = ctx_files

    copied, missing = [], []
    for name in templates_for(args.mode):
        src = os.path.join(TEMPLATE_DIR, name)
        dst = os.path.join(session_dir, name)
        if not os.path.exists(src):
            missing.append(name)
            continue
        if os.path.exists(dst) and not args.force:
            continue
        shutil.copyfile(src, dst)
        copied.append(name)

    with open(os.path.join(session_dir, "session.json"), "w", encoding="utf-8") as fh:
        json.dump(session, fh, indent=2)
        fh.write("\n")

    print("session:   %s (%s mode)" % (args.session_id, args.mode))
    print("directory: %s" % session_dir)
    print("stages:    run %s | skipped %s" % (session["stages"]["planned"], session["stages"]["skipped"]))
    if tier == 0:
        print("context:   tier 0 — wb/context/ absent or empty.")
        print("           Dimensions 4 (strategic fit) and 6 (falsifiability) will be")
        print("           emitted as questions, not verdicts.")
    else:
        print("context:   tier 1 — %d file(s): %s" % (len(ctx_files), ", ".join(ctx_files)))
    print("templates: %d copied" % len(copied))
    if missing:
        print("warning:   templates not found: %s" % ", ".join(missing), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
