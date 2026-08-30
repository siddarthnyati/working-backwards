#!/usr/bin/env python3
"""Verify a session's traceability: every requirement's Source: line must point at
something that exists — a PR paragraph anchor, an FAQ entry, a blocker, a demo failure
state, or an artifact file. Also reconciles requirements against release slices.

Usage: python verify_sources.py wb/<session-id>

Exit 0 when every citation resolves and no slice cites a missing requirement.
Standard library only.
"""
import os, re, sys

def main(d):
    read = lambda f: open(os.path.join(d, f), encoding="utf-8").read() if os.path.exists(os.path.join(d, f)) else ""
    pr, efaq, ifaq, rfaq = read("01-press-release.md"), read("02-faq-external.md"), read("02-faq-internal.md"), read("02-faq-regional.md")
    demo, blockers, reqs, plan = read("03-demo-spec.md"), read("BLOCKERS.md"), read("06-requirements.md"), read("07-release-plan.md")

    def exists(token):
        m = re.fullmatch(r"PR ¶(\d+)", token)
        if m:   return ("**¶%s**" % m.group(1)) in pr
        if re.fullmatch(r"EFAQ-\d+", token):  return re.search(r"^%s ·" % token, efaq, re.M) is not None
        if re.fullmatch(r"IFAQ-\d+", token):  return re.search(r"^%s ·" % token, ifaq, re.M) is not None
        if re.fullmatch(r"RFAQ-\d+", token):  return re.search(r"^%s ·" % token, rfaq, re.M) is not None
        if re.fullmatch(r"BLK-\d+", token):   return re.search(r"^%s ·" % token, blockers, re.M) is not None
        m = re.fullmatch(r"03-demo-spec\.md (F\d+)", token)
        if m:   return re.search(r"\|\s*%s\s*\|" % m.group(1), demo) is not None
        if re.fullmatch(r"0\d-[a-z-]+\.md", token): return os.path.exists(os.path.join(d, token))
        return None  # unrecognised citation shape

    blocks = re.findall(r"^(REQ-(?:D|DP)\d+) · (.+?)$(.*?)(?=^```|\Z)", reqs, re.M | re.S)
    fail = unrec = checked = 0
    for rid, title, body in blocks:
        m = re.search(r"^Source: (.+)$", body, re.M)
        if not m:
            print("  X  %s — no Source: line" % rid); fail += 1; continue
        src = m.group(1).strip()
        if src.upper().startswith("NONE"):
            print("  note: %s — Source: NONE (declared flagged)" % rid); continue
        for tok in [t.strip() for t in src.split("/")]:
            r = exists(tok); checked += 1
            if r is None:  print("  ?  %s cites %r — unrecognised shape" % (rid, tok)); unrec += 1
            elif not r:    print("  X  %s cites %r — TARGET DOES NOT EXIST" % (rid, tok)); fail += 1

    slice_reqs = set()
    for m in re.finditer(r"^Requirements: (.+)$", plan, re.M):
        slice_reqs |= set(re.findall(r"REQ-(?:D|DP)\d+", m.group(1)))
    all_reqs = {b[0] for b in blocks}
    ghosts, orphans = slice_reqs - all_reqs, all_reqs - slice_reqs

    print("requirements parsed ......... %d" % len(blocks))
    print("citations checked ........... %d" % checked)
    print("broken citations ............ %d" % fail)
    print("unrecognised shapes ......... %d" % unrec)
    print("slice cites a missing REQ ... %s" % (sorted(ghosts) or "none"))
    print("REQ in no slice ............. %s" % (sorted(orphans) or "none"))
    return 1 if (fail or unrec or ghosts) else 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__); raise SystemExit(2)
    raise SystemExit(main(sys.argv[1]))
