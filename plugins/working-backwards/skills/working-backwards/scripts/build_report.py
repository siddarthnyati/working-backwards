#!/usr/bin/env python3
"""Compile a Working Backwards session into one interactive HTML report.

Reads wb/<session-id>/ and writes report.html next to the artifacts (or -o path):
a self-contained page — no network, no build step — with the confidence numbers,
stage verdicts, blocker cards, filterable requirements, the release DAG, the
question list, the judge log, and every raw artifact embedded.

Usage:
    python build_report.py wb/<session-id> [-o report.html]

Standard library only.
"""
import argparse, datetime, html, json, os, re, sys

FIELD_RE = re.compile(r"^\s*([A-Za-z][A-Za-z ]{2,30}?):\s*(.*)$")
GWT_RE = re.compile(r"^\s*(GIVEN|WHEN|THEN|AND)\b\s*(.*)$")
REQ_RE = re.compile(r"^(REQ-(?:D|DP)\d+) · (.+?)$")
BLK_RE = re.compile(r"^(BLK-\d+) · ([A-Z]+) · severity:\s*(\w+)")
SLICE_RE = re.compile(r"^(R\d+) · (.+?)$")

def read(d, f):
    p = os.path.join(d, f)
    return open(p, encoding="utf-8").read() if os.path.exists(p) else ""

def parse_blockers(text):
    out, cur = [], None
    for ln in text.splitlines():
        m = BLK_RE.match(ln.strip())
        if m:
            cur = {"id": m.group(1), "cat": m.group(2), "sev": m.group(3),
                   "ask": "", "owner": "", "blocks": "", "status": "OPEN", "surfaced": ""}
            out.append(cur); continue
        if cur is None: continue
        s = ln.strip()
        for key, field in [("Ask:", "ask"), ("Owner role:", "owner"),
                           ("Blocks:", "blocks"), ("Status:", "status"), ("Surfaced by:", "surfaced")]:
            if s.startswith(key):
                cur[field] = s[len(key):].strip(); break
        else:
            if cur["ask"] and not cur["owner"] and s and not s.startswith("```"):
                cur["ask"] += " " + s
    return out

def parse_questions(text):
    out = []
    for ln in text.splitlines():
        cells = [c.strip() for c in ln.split("|")]
        if len(cells) >= 5 and cells[1].startswith("Q-"):
            out.append({"id": cells[1], "q": cells[3] if len(cells) > 5 else cells[2],
                        "ask": cells[4] if len(cells) > 5 else cells[3],
                        "status": (cells[5] if len(cells) > 5 else cells[4]) or "OPEN"})
    return out

def parse_reqs(text):
    lines = [l for l in text.splitlines() if not l.strip().startswith("```")]
    out, cur, in_ac = [], None, False
    for raw in lines:
        m = REQ_RE.match(raw.strip())
        if m and not raw.strip().startswith("|"):
            cur = {"id": m.group(1), "title": m.group(2), "source": "", "statement": "",
                   "gwt": [], "flags": [], "depends": ""}
            out.append(cur); in_ac = False; continue
        if cur is None: continue
        if GWT_RE.match(raw):
            cur["gwt"].append(raw.strip()); in_ac = True; continue
        fm = FIELD_RE.match(raw)
        if fm:
            k, v = fm.group(1).lower(), fm.group(2).strip()
            if k == "source":
                cur["source"] = v
                if v.upper().startswith("NONE"): cur["flags"].append("unsourced")
            elif k == "statement": cur["statement"] = v
            elif k == "provenance" and "RESTS ON ASSUMPTION" in v: cur["flags"].append("assumption")
            elif k == "status" and "SHAPE PENDING" in v.upper(): cur["flags"].append("shape-pending")
            elif k == "depends on": cur["depends"] = v
            in_ac = False
    for r in out:
        r["kind"] = "discovery" if r["id"].startswith("REQ-D") and not r["id"].startswith("REQ-DP") else "delivery"
    return out

def parse_slices(text):
    lines = [l for l in text.splitlines() if not l.strip().startswith("```")]
    out, cur = [], None
    for raw in lines:
        m = SLICE_RE.match(raw.strip())
        if m and "->" not in raw and not raw.strip().startswith(("|", ">")):
            cur = {"id": m.group(1), "title": m.group(2), "reqs": "", "ships": "", "blocked": ""}
            out.append(cur); continue
        if cur is None: continue
        fm = FIELD_RE.match(raw)
        if fm:
            k, v = fm.group(1).lower(), fm.group(2).strip()
            if k == "requirements": cur["reqs"] = v
            elif k == "ships": cur["ships"] = v
            elif k == "blocked by": cur["blocked"] = "" if v in ("—", "-", "") else v
    return out

def dag_block(text):
    m = re.search(r"## Dependency DAG\s*```\n(.*?)```", text, re.S)
    return m.group(1).rstrip() if m else ""

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__ — Working Backwards report</title>
<style>
:root{--paper:#f2eee5;--paper-2:#eae5d9;--ink:#1c1815;--ink-2:#4a423a;--ink-3:#7d7263;
--rule:#cdc4b1;--accent:#9c2f1c;--accent-soft:#f0d9d2;--accent-ink:#7a2415;
--ok:#3d5a3f;--ok-soft:#dde5d9;
--mono:"SF Mono",ui-monospace,Menlo,Consolas,monospace;
--serif:"Iowan Old Style",Palatino,Georgia,serif}
@media (prefers-color-scheme:dark){:root{--paper:#16130f;--paper-2:#1e1a15;--ink:#ece5d8;
--ink-2:#b8ae9d;--ink-3:#8a7f6e;--rule:#3a3227;--accent:#e2705a;--accent-soft:#3a1f18;
--accent-ink:#f0917d;--ok:#9dbb9a;--ok-soft:#24301f}}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--serif);
font-size:17px;line-height:1.55;overflow-x:hidden}
.wrap{max-width:64rem;margin:0 auto;padding:0 1.2rem}
header{padding:2.4rem 0 1.4rem;border-bottom:1px solid var(--rule)}
h1{font-weight:400;font-size:1.9rem;margin:0 0 .3rem;letter-spacing:-.02em}
h4{font-family:var(--mono);font-weight:500;font-size:.68rem;letter-spacing:.1em;
text-transform:uppercase;color:var(--ink-3);margin:0 0 .6rem}
.meta{font-family:var(--mono);font-size:.7rem;color:var(--ink-3)}
.nums{display:grid;grid-template-columns:repeat(auto-fit,minmax(8.5rem,1fr));gap:0;
border:1px solid var(--rule);border-right:0;margin:1.4rem 0}
.num{border-right:1px solid var(--rule);padding:.7rem .9rem;background:var(--paper-2)}
.num b{display:block;font-size:1.5rem;font-weight:400}
.num span{font-family:var(--mono);font-size:.62rem;color:var(--ink-3);letter-spacing:.06em;
text-transform:uppercase;line-height:1.3;display:block}
.stagebar{display:flex;gap:2px;margin:0 0 1.4rem;flex-wrap:wrap}
.sb{font-family:var(--mono);font-size:.64rem;padding:.35rem .55rem;border:1px solid var(--rule);
background:var(--paper-2);color:var(--ink-2)}
.sb.rev{border-color:var(--accent);color:var(--accent-ink)}
nav{display:flex;gap:0;border:1px solid var(--rule);width:max-content;max-width:100%;
overflow-x:auto;margin:1.2rem 0}
nav button{font-family:var(--mono);font-size:.7rem;padding:.5rem .9rem;background:none;border:0;
border-right:1px solid var(--rule);cursor:pointer;color:var(--ink-3);white-space:nowrap}
nav button:last-child{border-right:0}
nav button[aria-pressed=true]{background:var(--ink);color:var(--paper)}
main{padding:1.2rem 0 3rem}
.tab{display:none}.tab.on{display:block}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(17rem,1fr));gap:0;
border:1px solid var(--rule);border-right:0;border-bottom:0}
.card{border-right:1px solid var(--rule);border-bottom:1px solid var(--rule);padding:1rem;min-width:0}
.card .h{font-family:var(--mono);font-size:.64rem;letter-spacing:.08em;color:var(--accent);
display:flex;justify-content:space-between;margin-bottom:.5rem}
.card .h .sev{color:var(--ink-3)}
.card p{font-size:.85rem;color:var(--ink-2);margin:0 0 .6rem}
.card .own{font-family:var(--mono);font-size:.64rem;color:var(--ink-2);border-top:1px solid var(--rule);
padding-top:.45rem}.card .own .st{float:right;color:var(--accent)}
.filters{display:flex;gap:.4rem;flex-wrap:wrap;margin:0 0 1rem}
.fc{font-family:var(--mono);font-size:.66rem;padding:.3rem .6rem;border:1px solid var(--rule);
background:var(--paper);cursor:pointer;color:var(--ink-2)}
.fc[aria-pressed=true]{background:var(--ink);color:var(--paper);border-color:var(--ink)}
.req{border:1px solid var(--rule);padding:.8rem .95rem;margin-bottom:.6rem;background:var(--paper-2)}
.req .rid{font-family:var(--mono);font-size:.74rem}
.req .flags{float:right}
.badge{font-family:var(--mono);font-size:.58rem;letter-spacing:.05em;border:1px solid var(--accent);
color:var(--accent-ink);background:var(--accent-soft);padding:.08rem .4rem;margin-left:.3rem}
.req .src{font-family:var(--mono);font-size:.64rem;color:var(--accent-ink);display:block;margin:.2rem 0 .4rem}
.req .st{font-size:.86rem;color:var(--ink-2);margin:0 0 .4rem}
.req pre{font-family:var(--mono);font-size:.66rem;line-height:1.55;color:var(--ink-2);
white-space:pre-wrap;margin:0}
table{border-collapse:collapse;width:100%;font-size:.82rem}
th,td{text-align:left;padding:.45rem .6rem;border-bottom:1px solid var(--rule);vertical-align:top}
th{font-family:var(--mono);font-size:.62rem;letter-spacing:.08em;text-transform:uppercase;
color:var(--ink-3);font-weight:500}
pre.mono{font-family:var(--mono);font-size:.72rem;line-height:1.6;white-space:pre-wrap;
background:var(--paper-2);border:1px solid var(--rule);padding:1rem;overflow-x:auto}
pre.dag{white-space:pre;font-family:var(--mono);font-size:.76rem;background:var(--paper-2);
border:1px solid var(--rule);padding:1rem;overflow-x:auto}
details{border:1px solid var(--rule);margin-bottom:.5rem;background:var(--paper-2)}
summary{font-family:var(--mono);font-size:.72rem;padding:.55rem .8rem;cursor:pointer;color:var(--ink-2)}
details pre{margin:0;border:0;border-top:1px solid var(--rule);max-height:26rem;overflow:auto}
.note{font-size:.8rem;color:var(--ink-3)}
.scroll{overflow-x:auto}
@media(max-width:700px){body{font-size:16px}.req .flags{float:none;display:block;margin:.3rem 0 0}}
</style></head><body>
<header><div class="wrap">
<h1>__TITLE__</h1>
<div class="meta">Working Backwards session report · __SID__ · __MODE__ mode · tier __TIER__ · generated __DATE__ by build_report.py — every number below is parsed from the artifacts, not typed</div>
<div class="nums" id="nums"></div>
<div class="stagebar" id="stagebar"></div>
<nav id="nav"></nav>
</div></header>
<main><div class="wrap">
<div class="tab" data-t="overview">
  <h4>Open blockers — questions with owners, never findings</h4>
  <div class="cards" id="blk"></div>
  <p class="note" style="margin-top:1rem">Status is only ever changed by a human. Nothing on this page resolves itself.</p>
</div>
<div class="tab" data-t="requirements">
  <div class="filters" id="rfilters"></div>
  <div id="reqs"></div>
</div>
<div class="tab" data-t="release">
  <h4>Dependency DAG</h4><pre class="dag" id="dag"></pre>
  <h4 style="margin-top:1.4rem">Slices</h4><div class="scroll"><table id="slices"></table></div>
</div>
<div class="tab" data-t="questions">
  <div class="scroll"><table id="qs"></table></div>
</div>
<div class="tab" data-t="judge">
  <h4>The judge log — every verdict and override, in order</h4>
  <pre class="mono" id="decisions"></pre>
</div>
<div class="tab" data-t="artifacts">
  <h4>Every artifact, as written to disk</h4>
  <div id="arts"></div>
</div>
</div></main>
<script type="application/json" id="data">__DATA__</script>
<script>
"use strict";
const D=JSON.parse(document.getElementById("data").textContent);
const $=s=>document.querySelector(s);
const esc=s=>s.replace(/&/g,"&amp;").replace(/</g,"&lt;");
const nums=[["claims observed",D.counts.observed],["assumed",D.counts.assumed],
 ["requirements",D.reqs.length],["flagged",D.reqs.filter(r=>r.flags.length).length],
 ["blockers open",D.blockers.filter(b=>b.status.startsWith("OPEN")).length],
 ["questions open",D.questions.filter(q=>q.status.startsWith("OPEN")).length]];
$("#nums").innerHTML=nums.map(([l,v])=>`<div class="num"><b>${v??"—"}</b><span>${l}</span></div>`).join("");
$("#stagebar").innerHTML=(D.verdicts||[]).map(v=>
 `<span class="sb${/REVISE|BLOCK/.test(v.verdict)?" rev":""}">S${v.stage} ${v.verdict}${v.overridden?" → OVERRIDDEN":""}${v.resolved?" → fixed":""}</span>`).join("");
const TABS=[["overview","Overview"],["requirements","Requirements"],["release","Release plan"],
 ["questions","Questions"],["judge","Judge log"],["artifacts","Artifacts"]];
$("#nav").innerHTML=TABS.map(([k,l],i)=>`<button data-k="${k}" aria-pressed="${i===0}">${l}</button>`).join("");
function show(k){document.querySelectorAll(".tab").forEach(t=>t.classList.toggle("on",t.dataset.t===k));
 document.querySelectorAll("#nav button").forEach(b=>b.setAttribute("aria-pressed",b.dataset.k===k))}
document.querySelectorAll("#nav button").forEach(b=>b.onclick=()=>show(b.dataset.k));
show("overview");
$("#blk").innerHTML=D.blockers.map(b=>`<div class="card">
 <div class="h"><span>${b.id} · ${b.cat}</span><span class="sev">${b.sev}</span></div>
 <p>${esc(b.ask)}</p>
 <div class="own">Ask: ${esc(b.owner)}<span class="st">${b.status}</span><br><span style="color:var(--ink-3)">Blocks: ${esc(b.blocks||"—")}</span></div></div>`).join("");
const FLT=[["all","all"],["discovery","discovery"],["delivery","delivery"],["flagged","flagged"]];
let cur="all";
$("#rfilters").innerHTML=FLT.map(([k,l],i)=>`<button class="fc" data-k="${k}" aria-pressed="${i===0}">${l}</button>`).join("");
function drawReqs(){
 const rs=D.reqs.filter(r=>cur==="all"||(cur==="flagged"?r.flags.length:r.kind===cur));
 $("#reqs").innerHTML=rs.map(r=>`<div class="req">
  <span class="flags">${r.flags.map(f=>`<span class="badge">${f}</span>`).join("")}</span>
  <span class="rid">${r.id} · ${esc(r.title)}</span>
  <span class="src">Source: ${esc(r.source||"—")}</span>
  <p class="st">${esc(r.statement)}</p>
  ${r.gwt.length?`<pre>${esc(r.gwt.join("\\n"))}</pre>`:""}</div>`).join("")||"<p class='note'>none</p>";
 document.querySelectorAll("#rfilters .fc").forEach(b=>b.setAttribute("aria-pressed",b.dataset.k===cur));
}
document.querySelectorAll("#rfilters .fc").forEach(b=>b.onclick=()=>{cur=b.dataset.k;drawReqs()});
drawReqs();
$("#dag").textContent=D.dag||D.edges.map(e=>e.join(" -> ")).join("\\n")||"(none)";
$("#slices").innerHTML="<tr><th></th><th>ships</th><th>requirements</th><th>status</th></tr>"+
 D.slices.map(s=>`<tr><td><code>${s.id}</code> ${esc(s.title)}</td><td>${esc(s.ships)}</td>
 <td style="font-family:var(--mono);font-size:.68rem">${esc(s.reqs)}</td>
 <td style="${s.blocked?"color:var(--accent)":""}">${s.blocked?"blocked — "+esc(s.blocked):"schedulable"}</td></tr>`).join("");
$("#qs").innerHTML="<tr><th>id</th><th>question</th><th>ask</th><th>status</th></tr>"+
 D.questions.map(q=>`<tr><td><code>${q.id}</code></td><td>${esc(q.q)}</td><td>${esc(q.ask)}</td><td>${q.status}</td></tr>`).join("");
$("#decisions").textContent=D.docs["DECISIONS.md"]||"(no DECISIONS.md)";
$("#arts").innerHTML=Object.keys(D.docs).map(f=>
 `<details><summary>${f}</summary><pre class="mono">${esc(D.docs[f])}</pre></details>`).join("");
</script></body></html>"""

def main(argv=None):
    p = argparse.ArgumentParser(description="Compile a WB session to an interactive HTML report.")
    p.add_argument("session_dir")
    p.add_argument("-o", "--output", default=None)
    a = p.parse_args(argv)
    d = a.session_dir

    sess = {}
    sj = read(d, "session.json")
    if sj:
        try: sess = json.loads(sj)
        except ValueError: pass

    docs = {}
    for f in sorted(os.listdir(d)):
        if f.endswith((".md", ".csv", ".json")) and os.path.isfile(os.path.join(d, f)):
            docs[f] = read(d, f)

    plan = read(d, "07-release-plan.md")
    claims = sess.get("claims", {})
    data = {
        "blockers": parse_blockers(read(d, "BLOCKERS.md")),
        "questions": parse_questions(read(d, "QUESTIONS.md")),
        "reqs": parse_reqs(read(d, "06-requirements.md")),
        "slices": parse_slices(plan),
        "edges": re.findall(r"^(R\d+) -> (R\d+)$", plan, re.M),
        "dag": dag_block(plan),
        "verdicts": (sess.get("critic") or {}).get("verdicts", []),
        "counts": {"observed": claims.get("observed"), "assumed": claims.get("assumed")},
        "docs": docs,
    }

    out = TEMPLATE
    out = out.replace("__TITLE__", html.escape(sess.get("initiative", os.path.basename(os.path.abspath(d)))))
    out = out.replace("__SID__", html.escape(sess.get("session_id", "?")))
    out = out.replace("__MODE__", html.escape(sess.get("mode", "?")))
    out = out.replace("__TIER__", str((sess.get("context") or {}).get("tier", "?")))
    out = out.replace("__DATE__", datetime.date.today().isoformat())
    out = out.replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))

    dest = a.output or os.path.join(d, "report.html")
    with open(dest, "w", encoding="utf-8") as fh:
        fh.write(out)
    print("wrote %s (%d KB) — %d blockers, %d requirements, %d questions, %d artifacts embedded"
          % (dest, len(out.encode()) // 1024, len(data["blockers"]), len(data["reqs"]),
             len(data["questions"]), len(docs)))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
