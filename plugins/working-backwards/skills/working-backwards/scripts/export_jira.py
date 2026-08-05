#!/usr/bin/env python3
"""Export a Working Backwards session to a JIRA-importable CSV.

Reads 06-requirements.md and 07-release-plan.md from a session directory and writes
jira-import.csv: one Epic row per release slice, one Story row per requirement,
epics before their stories.

The Source: line is preserved verbatim in the Description. Traceability has to
survive the export or it dies at the import, which is the whole point.

Usage:
    python export_jira.py wb/<session-id> [-o jira-import.csv] [--no-ac-field]

Standard library only.
"""

import argparse
import csv
import os
import re
import sys

# The separator excludes "->" so a dependency edge list ("R1 -> R2") is not mistaken for a
# slice header. Templates use "·"; ":", em dash and a bare hyphen are accepted for tolerance.
REQ_RE = re.compile(r"^#*\s*(REQ-(?:D|DP)\d+)\s*(?:[·:—]|-(?!>))\s*(.+?)\s*$")
SLICE_RE = re.compile(r"^#*\s*(R\d+)\s*(?:[·:—]|-(?!>))\s*(.+?)\s*$")
FIELD_RE = re.compile(r"^\s*([A-Za-z][A-Za-z ]{2,30}?):\s*(.*)$")
GWT_RE = re.compile(r"^\s*(GIVEN|WHEN|THEN|AND)\b\s*(.*)$", re.IGNORECASE)
ID_RE = re.compile(r"(REQ-(?:D|DP)\d+|BLK-\d+|R\d+)")

COLUMNS = [
    "Issue Type",
    "Summary",
    "Description",
    "Acceptance Criteria",
    "Epic Name",
    "Parent",
    "Labels",
    "Priority",
]

SEVERITY_PRIORITY = {"high": "Highest", "medium": "High", "low": "Medium"}


def strip_fences(lines):
    """Drop ``` fence markers so blocks parse whether or not they're fenced."""
    return [ln for ln in lines if not ln.lstrip().startswith("```")]


def parse_blocks(path, header_re):
    """Parse 'ID · Title' blocks with 'Field: value' lines and a GIVEN/WHEN/THEN body."""
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as fh:
        lines = strip_fences(fh.read().splitlines())

    blocks, current, in_ac = [], None, False
    for raw in lines:
        m = header_re.match(raw)
        if m and not raw.lstrip().startswith(("|", ">")):
            if current:
                blocks.append(current)
            current = {"id": m.group(1), "title": m.group(2), "fields": {}, "ac": [], "bullets": []}
            in_ac = False
            continue
        if current is None:
            continue

        if GWT_RE.match(raw):
            current["ac"].append(raw.strip())
            in_ac = True
            continue

        fm = FIELD_RE.match(raw)
        if fm:
            key, val = fm.group(1).strip().lower(), fm.group(2).strip()
            if key.startswith("acceptance"):
                in_ac = True
                if val:
                    current["ac"].append(val)
                continue
            current["fields"][key] = val
            in_ac = False
            continue

        stripped = raw.strip()
        if not stripped:
            in_ac = False
            continue
        if stripped.startswith(("-", "*")):
            current["bullets"].append(stripped.lstrip("-* ").strip())
        elif in_ac:
            current["ac"].append(stripped)

    if current:
        blocks.append(current)
    return blocks


def ids_in(text):
    return ID_RE.findall(text or "")


def blocker_severities(path):
    """Map BLK id -> severity from BLOCKERS.md, for priority on blocked work."""
    sev = {}
    if not os.path.exists(path):
        return sev
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            m = re.search(r"(BLK-\d+).*?severity:?\s*(high|medium|low)", line, re.IGNORECASE)
            if m:
                sev[m.group(1)] = m.group(2).lower()
                continue
            cells = [c.strip() for c in line.split("|")]
            if len(cells) > 4 and cells[1].startswith("BLK-"):
                if cells[3].lower() in SEVERITY_PRIORITY:
                    sev[cells[1]] = cells[3].lower()
    return sev


def description_for(req):
    f = req["fields"]
    parts = []
    if f.get("statement"):
        parts.append(f["statement"])
    if f.get("source"):
        parts.append("Source: %s" % f["source"])
    if f.get("provenance"):
        parts.append("Provenance: %s" % f["provenance"])
    if f.get("out of scope"):
        parts.append("Out of scope: %s" % f["out of scope"])
    if f.get("depends on"):
        parts.append("Depends on: %s" % f["depends on"])
    if f.get("conditional on"):
        parts.append("Conditional on: %s" % f["conditional on"])
    return "\n\n".join(parts)


def labels_for(req, slice_blocked):
    labels = ["working-backwards"]
    labels.append("discovery" if req["id"].startswith("REQ-D") and not req["id"].startswith("REQ-DP") else "delivery")
    blob = " ".join([req["fields"].get("provenance", ""), req["fields"].get("status", "")]).lower()
    if "rests on assumption" in blob:
        labels.append("rests-on-assumption")
    if "shape pending" in blob:
        labels.append("shape-pending")
    if slice_blocked:
        labels.append("blocked")
    return " ".join(labels)


def priority_for(depends_on, severities):
    worst = None
    for blk in [i for i in ids_in(depends_on) if i.startswith("BLK-")]:
        sev = severities.get(blk)
        if sev and (worst is None or list(SEVERITY_PRIORITY).index(sev) < list(SEVERITY_PRIORITY).index(worst)):
            worst = sev
    return SEVERITY_PRIORITY.get(worst, "Medium")


def build_rows(reqs, slices, severities, ac_field=True):
    by_id = {r["id"]: r for r in reqs}
    rows, placed = [], set()

    for sl in slices:
        blocked_by = sl["fields"].get("blocked by", "").strip()
        is_blocked = bool([i for i in ids_in(blocked_by) if i.startswith("BLK-")])

        epic_desc = []
        if sl["fields"].get("ships"):
            epic_desc.append("Ships: %s" % sl["fields"]["ships"])
        if sl["fields"].get("requirements"):
            epic_desc.append("Requirements: %s" % sl["fields"]["requirements"])
        if sl["fields"].get("depends on"):
            epic_desc.append("Depends on: %s" % sl["fields"]["depends on"])
        if is_blocked:
            epic_desc.append("Blocked by: %s" % blocked_by)
        if sl["bullets"]:
            epic_desc.append("Test harness:\n" + "\n".join("- " + b for b in sl["bullets"]))

        epic_labels = "working-backwards release-slice" + (" blocked" if is_blocked else "")
        rows.append({
            "Issue Type": "Epic",
            "Summary": "%s · %s" % (sl["id"], sl["title"]),
            "Description": "\n\n".join(epic_desc),
            "Acceptance Criteria": "",
            "Epic Name": "%s %s" % (sl["id"], sl["title"]),
            "Parent": "",
            "Labels": epic_labels,
            "Priority": priority_for(blocked_by, severities) if is_blocked else "Medium",
        })

        for rid in ids_in(sl["fields"].get("requirements", "")):
            req = by_id.get(rid)
            if req is None:
                continue
            placed.add(rid)
            ac = "\n".join(req["ac"])
            desc = description_for(req)
            if not ac_field and ac:
                desc = desc + "\n\nAcceptance criteria:\n" + ac
            rows.append({
                "Issue Type": "Story",
                "Summary": "%s · %s" % (req["id"], req["title"]),
                "Description": desc,
                "Acceptance Criteria": ac if ac_field else "",
                "Epic Name": "",
                "Parent": "%s %s" % (sl["id"], sl["title"]),
                "Labels": labels_for(req, is_blocked),
                "Priority": priority_for(req["fields"].get("depends on", ""), severities),
            })

    orphans = [r for r in reqs if r["id"] not in placed]
    for req in orphans:
        ac = "\n".join(req["ac"])
        desc = description_for(req)
        if not ac_field and ac:
            desc = desc + "\n\nAcceptance criteria:\n" + ac
        rows.append({
            "Issue Type": "Story",
            "Summary": "%s · %s" % (req["id"], req["title"]),
            "Description": desc,
            "Acceptance Criteria": ac if ac_field else "",
            "Epic Name": "",
            "Parent": "",
            "Labels": labels_for(req, False) + " unsliced",
            "Priority": priority_for(req["fields"].get("depends on", ""), severities),
        })
    return rows, orphans


def main(argv=None):
    p = argparse.ArgumentParser(description="Export a WB session to jira-import.csv")
    p.add_argument("session_dir", help="path to wb/<session-id>")
    p.add_argument("-o", "--output", default=None, help="default: <session_dir>/jira-import.csv")
    p.add_argument(
        "--no-ac-field",
        action="store_true",
        help="target instance has no Acceptance Criteria field; fold it into Description",
    )
    args = p.parse_args(argv)

    d = args.session_dir
    reqs = parse_blocks(os.path.join(d, "06-requirements.md"), REQ_RE)
    slices = parse_blocks(os.path.join(d, "07-release-plan.md"), SLICE_RE)
    severities = blocker_severities(os.path.join(d, "BLOCKERS.md"))

    if not reqs:
        print("error: no requirements found in %s/06-requirements.md" % d, file=sys.stderr)
        return 1

    rows, orphans = build_rows(reqs, slices, severities, ac_field=not args.no_ac_field)
    out = args.output or os.path.join(d, "jira-import.csv")

    with open(out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=COLUMNS, quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

    epics = sum(1 for r in rows if r["Issue Type"] == "Epic")
    print("wrote %s" % out)
    print("  %d epic(s), %d story(ies)" % (epics, len(rows) - epics))

    unsourced = [r["id"] for r in reqs if not r["fields"].get("source") or "NONE" in r["fields"]["source"].upper()]
    if unsourced:
        print("  warning: no valid Source: line — %s" % ", ".join(unsourced), file=sys.stderr)
    if orphans:
        print("  warning: in no release slice — %s" % ", ".join(o["id"] for o in orphans), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
