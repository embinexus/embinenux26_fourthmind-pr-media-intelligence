"""Generates the Fourth Mind architecture page (hand-built inline SVG diagram + tech-stack table).

Usage: python3 tools/architecture/build_architecture.py dist/architecture/index.html
"""
from html import escape as esc

INK = "#16203a"; MUTED = "#5b6677"; LINE = "#cfd8e6"; SOFT = "#f6f8fc"
OR = "#ff8702"; OR_D = "#c25f00"; OR_BG = "#fff3e6"
BL = "#1e3a8a"; BL_BG = "#e8effc"; BL_LN = "#c7d5f3"
RED = "#b91c1c"; RED_BG = "#fdecec"; GRN = "#15803d"
WARN_BG = "#fff7ed"; WARN_LN = "#f6cf9f"

W, H = 1640, 1030
out = []

def rect(x, y, w, h, fill="#fff", stroke=LINE, rx=10, sw=1, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')

def text(x, y, s, size=11, weight=400, fill=INK, anchor="start", fam="Roboto", ls=None, rot=None, halo=False):
    fams = {"Roboto": "Roboto, system-ui, sans-serif", "Mont": "Montserrat, system-ui, sans-serif",
            "Mono": "'Roboto Mono', ui-monospace, monospace"}[fam]
    extra = f' letter-spacing="{ls}"' if ls else ""
    if rot is not None:
        extra += f' transform="rotate({rot} {x} {y})"'
    if halo:
        extra += ' stroke="#ffffff" stroke-width="4" stroke-linejoin="round" paint-order="stroke"'
    out.append(f'<text x="{x}" y="{y}" font-family="{fams}" font-size="{size}" font-weight="{weight}" '
               f'fill="{fill}" text-anchor="{anchor}"{extra}>{esc(s)}</text>')

def lane(x, y, s, color=OR_D):
    text(x, y, s.upper(), size=10.5, weight=700, fill=color, fam="Mono", ls="1.4")

def box(x, y, w, h, title, subs=(), fill="#fff", stroke=LINE, tcol=INK, scol=MUTED, sw=1, dash=None,
        tsize=12.5, ssize=10.5, pad=12, rx=10, mono_subs=False):
    rect(x, y, w, h, fill, stroke, rx=rx, sw=sw, dash=dash)
    text(x + pad, y + 22, title, size=tsize, weight=700, fill=tcol, fam="Mont")
    for i, s in enumerate(subs):
        text(x + pad, y + 40 + i * 15, s, size=ssize, fill=scol, fam="Mono" if mono_subs else "Roboto")

def chip(x, y, w, h, title, sub=None, fill=SOFT, stroke=LINE, tcol=INK, scol=MUTED, center=False, tsize=11.5):
    rect(x, y, w, h, fill, stroke, rx=8)
    if center:
        ty = y + h / 2 + (-2 if sub else 4)
        text(x + w / 2, ty, title, size=tsize, weight=700, fill=tcol, fam="Mont", anchor="middle")
        if sub:
            text(x + w / 2, ty + 15, sub, size=10, fill=scol, anchor="middle")
    else:
        text(x + 11, y + 19, title, size=tsize, weight=700, fill=tcol, fam="Mont")
        if sub:
            text(x + 11, y + 35, sub, size=10, fill=scol)

MK = {"ink": MUTED, "or": OR, "bl": BL, "red": RED}

def path(pts, kind="ink", end=True, start=False, dash=None, sw=1.5):
    d = "M" + " L".join(f"{px} {py}" for px, py in pts)
    col = MK[kind]
    a = f' marker-end="url(#m-{kind})"' if end else ""
    a += f' marker-start="url(#m-{kind}-s)"' if start else ""
    a += f' stroke-dasharray="{dash}"' if dash else ""
    out.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linejoin="round"{a}/>')

def label(x, y, s, kind="ink", anchor="middle", size=10, rot=None):
    text(x, y, s, size=size, weight=500, fill={"ink": MUTED, "or": OR_D, "bl": BL, "red": RED}[kind],
         anchor=anchor, fam="Mono", halo=True, rot=rot)

# ---------------- defs ----------------
defs = ['<defs>']
for k, c in MK.items():
    defs.append(f'<marker id="m-{k}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
                f'<path d="M0 0 L10 5 L0 10 z" fill="{c}"/></marker>')
    defs.append(f'<marker id="m-{k}-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
                f'<path d="M10 0 L0 5 L10 10 z" fill="{c}"/></marker>')
defs.append('<pattern id="dots" width="14" height="14" patternUnits="userSpaceOnUse"><circle cx="1.2" cy="1.2" r="1.2" fill="#e3e9f3"/></pattern>')
defs.append('</defs>')
out.extend(defs)
rect(0, 0, W, H, "url(#dots)", "none", rx=0, sw=0)

# ---------------- Column A: data sources ----------------
AX, AW = 20, 240
lane(AX, 88, "01 · Data sources")
A = [
    ("Embitel SDV Knowledge Repo", ["internal .docx", "company ground truth"]),
    ("embitel.com", ["50+ SDV service pages", "case studies · partners · awards"]),
    ("Competitor websites", ["KPIT · Tata Elxsi · Sasken", "LTTS · eInfochips"]),
    ("News & trade media", ["wire · Autocar Pro · ET Auto", "Just Auto · CXOToday"]),
    ("Analyst & event signals", ["ISG ratings · CES / IAA", "executive bylines"]),
    ("Brand assets", ["banner imagery · colour tokens", "#ff8702 orange · #1e3a8a blue"]),
]
AY = [100, 188, 276, 364, 452, 540]
for (t, s), y in zip(A, AY):
    box(AX, y, AW, 74, t, s)

# ---------------- Column B: ingestion ----------------
BX, BW = 320, 240
lane(BX, 88, "02 · Ingestion & retrieval")
box(BX, 100, BW, 74, "DOCX text extraction", ["python · repo → structured KB", "feeds CLAUDE.md"])
box(BX, 188, BW, 148, "WebFetch", ["HTML → clean text, per page", "meta-description recovery", "for JS-rendered / paywalled", "pages · company + rivals", "no page = no claim"])
box(BX, 356, BW, 54, "WebSearch", ["blocked by egress proxy · HTTP 403"], fill=RED_BG, stroke=RED, tcol=RED, scol=RED, dash="5 4")
box(BX, 424, BW, 102, "Bing News fallback", ["news queries routed via WebFetch", "direct article verification", "window: Sep 2025 – Sep 2026"])
rect(BX, 552, BW, 98, "#fff", LINE)
text(BX + 12, 574, "Provenance tagging", size=12.5, weight=700, fam="Mont")
text(BX + 12, 592, "every claim carries its source tag", size=10.5, fill=MUTED)
for i, (tag, col, bg) in enumerate([("REPOSITORY", BL, BL_BG), ("BROWSED", GRN, "#e9f6ee"),
                                     ("SYNOPSIS", OR_D, OR_BG), ("TITLE-ONLY", RED, RED_BG)]):
    cx = BX + 12 + (i % 2) * 110; cy = 604 + (i // 2) * 21
    rect(cx, cy, 102, 17, bg, "none", rx=4, sw=0)
    text(cx + 51, cy + 12.5, tag, size=9.5, weight=700, fill=col, fam="Mono", anchor="middle")

# A -> B arrows
path([(260, 137), (318, 137)]); label(289, 131, "parse")
path([(260, 225), (318, 225)]); label(289, 219, "fetch")
path([(260, 313), (318, 313)]); label(289, 307, "fetch")
path([(260, 383), (318, 383)], "red", dash="4 3")
text(289, 387.5, "✕", size=13, weight=700, fill=RED, anchor="middle", halo=True)
path([(260, 432), (318, 432)]); label(289, 426, "fallback", size=9.5)
path([(260, 500), (318, 500)]); label(289, 494, "query")

# evidence bus
BUS = 588
out.append(f'<path d="M{BUS} 137 L{BUS} 601" fill="none" stroke="{MUTED}" stroke-width="1.5"/>')
for y in (137, 262, 475):
    path([(560, y), (BUS, y)], end=False)
    out.append(f'<circle cx="{BUS}" cy="{y}" r="3" fill="{MUTED}"/>')
path([(560, 601), (BUS, 601)], end=False, dash="2 3")
out.append(f'<circle cx="{BUS}" cy="601" r="3" fill="{MUTED}"/>')

# ---------------- Human reviewer ----------------
rect(740, 16, 260, 58, OR_BG, OR, rx=12, sw=1.5)
text(870, 40, "Human reviewer · Embitel PR", size=13, weight=700, fam="Mont", anchor="middle")
text(870, 58, "signs off each checkpoint", size=10.5, fill=OR_D, anchor="middle")

# ---------------- Core container ----------------
CX, CW, CY, CH = 600, 720, 100, 584
rect(CX, CY, CW, CH, "#fbfcfe", BL, rx=16, sw=1.6)
lane(620, 128, "03 · Reasoning core", BL)
text(1300, 128, "THE FOURTH MIND", size=10.5, weight=700, fill=MUTED, fam="Mono", anchor="end", ls="1.4")

MODS = [
    ("MODULE 01", ["Company", "Understanding"], ["Ground-truth model", "SDV-only scope", "→ CLAUDE.md"]),
    ("MODULE 02", ["Competitor", "Radar"], ["5 validated rivals", "Confidence scoring", "Overlap vs. edge"]),
    ("MODULE 03", ["PR", "Intelligence"], ["Narrative · media", "Exec · events", "FACT/INSIGHT/OPP."]),
    ("MODULE 04", ["PR Analytics", "& Strategy"], ["Visibility matrix", "Positioning matrix", "White-space plays"]),
]
MX = [620, 803, 986, 1169]; MW = 130; MY = 146; MH = 150
for (badge, title, bullets), x in zip(MODS, MX):
    rect(x, MY, MW, MH, "#fff", OR, rx=12, sw=1.5)
    out.append(f'<path d="M{x} {MY+12} a12 12 0 0 1 12 -12 h{MW-24} a12 12 0 0 1 12 12 v14 h-{MW} z" fill="{OR_BG}"/>')
    text(x + 12, MY + 17, badge, size=9.5, weight=700, fill=OR_D, fam="Mono", ls="1.2")
    text(x + 12, MY + 46, title[0], size=13, weight=800, fam="Mont")
    text(x + 12, MY + 62, title[1], size=13, weight=800, fam="Mont")
    for i, b in enumerate(bullets):
        yy = MY + 88 + i * 18
        out.append(f'<circle cx="{x+15}" cy="{yy-3.5}" r="2" fill="{OR}"/>')
        text(x + 22, yy, b, size=10.5, fill=MUTED)

GY = MY + 75
for gx, n in ((776.5, "1"), (959.5, "2")):
    path([(gx - 26.5, GY), (gx + 24.5, GY)], "or", sw=1.6)
    out.append(f'<path d="M{gx} {GY-11} L{gx+11} {GY} L{gx} {GY+11} L{gx-11} {GY} z" fill="{OR}" stroke="#fff" stroke-width="1.5"/>')
    text(gx, GY + 4, "✓", size=11, weight=700, fill="#fff", anchor="middle")
    label(gx, GY + 28, f"gate {n}", "or", size=9.5)
path([(1116, GY), (1167, GY)]); label(1142, GY - 7, "feeds", size=9.5)

for gx in (776.5, 959.5):
    path([(gx, 74), (gx, GY - 13)], "or", dash="5 4", sw=1.4)
label(868, 92, "approve / revise", "or")

# evidence rail
RY = 322
path([(BUS, RY), (1051, RY)], end=False)
out.append(f'<circle cx="{BUS}" cy="{RY}" r="3" fill="{MUTED}"/>')
for x in MX[:3]:
    path([(x + 65, RY), (x + 65, MY + MH + 2)])
    out.append(f'<circle cx="{x+65}" cy="{RY}" r="2.6" fill="{MUTED}"/>')
label(1062, RY + 4, "provenance-tagged evidence", anchor="start")

def row(y_label, title, items, fill, stroke, tcol=INK, scol=MUTED):
    lane(620, y_label, title, MUTED)
    cw, gap = 161, 12
    for i, (t, s) in enumerate(items):
        chip(620 + i * (cw + gap), y_label + 10, cw, 48, t, s, fill=fill, stroke=stroke, tcol=tcol, scol=scol)

row(356, "Guardrails", [("SDV-only scope", "Digital Transf. excluded"), ("Rival rule", "service firms, not OEM/Tier-1"),
                        ("No fabrication", "gaps flagged, never filled"), ("Evidence per claim", "source URL + tag")],
    WARN_BG, WARN_LN)
row(442, "Skills (reusable instructions)", [("artifact-design", "tokens · type · layout"), ("artifact-capabilities", "window.claude db API"),
                                            ("artifact-diagramming", "inline SVG figures"), ("pr-competitive-intel", "custom workflow skill")],
    BL_BG, BL_LN)

lane(620, 528, "Agent loop", MUTED)
LX = [620, 762, 904, 1046, 1188]; LW = 112
for i, (x, s) in enumerate(zip(LX, ["Plan", "Retrieve", "Verify", "Synthesize", "Render"])):
    rect(x, 538, LW, 34, "#fff", BL, rx=17, sw=1.3)
    text(x + LW / 2, 559, s, size=11.5, weight=700, fill=BL, fam="Mont", anchor="middle")
    if i < 4:
        path([(x + LW, 555), (LX[i + 1] - 2, 555)], "bl", sw=1.3)
path([(1244, 572), (1244, 590), (676, 590), (676, 574)], "bl", sw=1.3, dash="4 3")
label(960, 594, "iterate on reviewer feedback", "bl", size=9.5)

lane(620, 616, "Runtime", MUTED)
for x, w, t in ((620, 220, "Claude · Sonnet 5 / Opus 5.5"), (850, 210, "Claude Agent SDK · Cowork"),
                (1070, 230, "Cloud sandbox · Python · Node")):
    rect(x, 626, w, 40, INK, INK, rx=8)
    text(x + w / 2, 650.5, t, size=11.5, weight=700, fill="#fff", fam="Mont", anchor="middle")

# ---------------- Persistence band ----------------
rect(600, 724, 720, 124, SOFT, LINE, rx=14)
lane(620, 744, "04 · Persistence & memory", BL)
PB = [(620, "Claude Project KB", ["CLAUDE.md + module docs", "memory across sessions"]),
      (850, "Session workspace", ["ephemeral cloud scratch", "patch scripts · screenshots"]),
      (1080, "Artifact shared DB", ["window.claude db capability", "competitors · activityLog"])]
for x, t, s in PB:
    box(x, 756, 220, 80, t, s, stroke=BL, sw=1.2)
path([(828, 686), (828, 754)], "bl", start=True, sw=1.4); label(834, 703, "read ground truth", "bl", anchor="start")
label(834, 716, "write module docs", "bl", anchor="start")
path([(960, 686), (960, 754)], "bl", start=True, sw=1.4); label(966, 709, "build files", "bl", anchor="start")
path([(1190, 686), (1190, 754)], "bl", start=True, sw=1.4); label(1196, 703, "rival list +", "bl", anchor="start")
label(1196, 716, "validation state", "bl", anchor="start")

# ---------------- Column D: presentation ----------------
DX, DW = 1360, 260
rect(DX, 100, DW, 600, "#fbfcfe", OR, rx=16, sw=1.6)
lane(DX + 20, 128, "05 · Presentation", OR_D)
text(DX + 20, 145, "hosted on claude.ai as Artifacts", size=10.5, fill=MUTED)
box(DX + 20, 160, 220, 80, "Module Hub", ["4-tab dashboard · sidebar nav", "banner heroes · published v4"])
box(DX + 20, 254, 220, 80, "PR Analytics Dashboard", ["visibility · positioning", "white-space recommendations"])
box(DX + 20, 348, 220, 80, "Competitor Radar (live)", ["keep / drop validation", "shared activity log"])
lane(DX + 20, 456, "Front-end stack", MUTED)
for i, t in enumerate(["HTML5 + CSS design tokens", "Vanilla JS · zero frameworks", "Inline SVG icons & diagrams",
                       "Montserrat · Roboto · Roboto Mono", "base64 imagery · CSP-safe", "Responsive ≤ 820px layout"]):
    rect(DX + 20, 466 + i * 36, 220, 28, "#fff", LINE, rx=7)
    out.append(f'<circle cx="{DX+34}" cy="{480+i*36}" r="3" fill="{OR}"/>')
    text(DX + 44, 484 + i * 36, t, size=10.5, fill=INK)

path([(1299, 200), (1378, 200)]); label(1339, 194, "render")
path([(1299, 280), (1378, 280)])

# DB <-> radar
path([(1300, 796), (1340, 796), (1340, 388), (1378, 388)], "bl", start=True, sw=1.4)
label(1334, 560, "live db sync", "bl", rot=-90)

# stakeholders
rect(1440, 730, 180, 110, "#fff", INK, rx=12, sw=1.3)
text(1456, 754, "Stakeholders", size=12.5, weight=700, fam="Mont")
for i, s in enumerate(["Embitel PR & leadership", "hackathon judges", "any browser · any device"]):
    text(1456, 774 + i * 16, s, size=10.5, fill=MUTED)
path([(1530, 700), (1530, 728)]); label(1536, 719, "view · share", anchor="start", size=9.5)

# ---------------- Build & QA band ----------------
rect(320, 874, 1300, 136, SOFT, LINE, rx=14, dash="6 4")
lane(340, 896, "06 · Build & QA toolchain")
BQ = [("Python patch scripts", "exact-match edits", "assert-guarded anchors"),
      ("base64 asset embedding", "banners → data: URIs", "no external image hosts"),
      ("Playwright + Chromium", "headless screenshots", "per-tab visual QA"),
      ("Section-diff regression", "every heading vs. baseline", "catches dropped content"),
      ("Versioned publish", "in-place artifact URL", "v1 → v4, one stable link")]
for i, (t, a, b) in enumerate(BQ):
    x = 340 + i * 252
    rect(x, 908, 240, 86, "#fff", LINE, rx=10)
    text(x + 12, 930, t, size=12, weight=700, fam="Mont")
    text(x + 12, 950, a, size=10.5, fill=MUTED)
    text(x + 12, 966, b, size=10.5, fill=MUTED)
    text(x + 228, 930, f"{i+1}", size=10, weight=700, fill=OR, fam="Mono", anchor="end")
    if i < 4:
        path([(x + 240, 951), (x + 250, 951)], sw=1.3)

path([(140, 614), (140, 951), (338, 951)]); label(146, 780, "brand banners", anchor="start")
path([(960, 836), (960, 872)], "bl", sw=1.3); label(966, 860, "scratch", "bl", anchor="start")
path([(1390, 906), (1390, 702)], "or", sw=1.6); label(1396, 860, "publish", "or", anchor="start")

svg = (f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="The Fourth Mind architecture: data sources are ingested and '
       f'provenance-tagged, a human-gated four-module Claude pipeline reasons over them, results persist in a project '
       f'knowledge base and artifact database, and render as hosted dashboards." xmlns="http://www.w3.org/2000/svg">'
       + "\n".join(out) + "</svg>")

TECH = [
    ("Reasoning", "Claude Sonnet 5 / Opus 5.5 (Anthropic)", "Research synthesis, competitor validation, PR analysis, dashboard authoring"),
    ("Orchestration", "Claude Agent SDK in Cowork mode", "Multi-step agent loop with tools, skills and human checkpoints"),
    ("Compute", "Isolated cloud sandbox (Linux, Python 3, Node.js)", "DOCX parsing, patch scripts, headless rendering"),
    ("Retrieval", "WebFetch · Bing News fallback route", "Page-level evidence; fallback when WebSearch was proxy-blocked (HTTP 403)"),
    ("Knowledge", "Claude Projects — CLAUDE.md + per-module docs", "Authoritative ground truth, persisted across sessions"),
    ("State", "Artifact db capability (window.claude)", "Shared competitor list, validation status, activity log"),
    ("Skills", "artifact-design · capabilities · diagramming · pr-competitive-intel", "Reusable instructions for design system, runtime API and the PR workflow"),
    ("Front end", "HTML5, CSS custom properties, vanilla JS, inline SVG", "Zero-dependency dashboards; base64 imagery for CSP-safe hosting"),
    ("Typography", "Google Fonts — Montserrat, Roboto, Roboto Mono", "Display, body and data faces"),
    ("QA", "Playwright + headless Chromium, section-diff checks", "Screenshot review per tab; regression check against the baseline"),
    ("Delivery", "claude.ai Artifacts (versioned, private → shareable)", "Module Hub, Competitor Radar, PR Analytics Dashboard"),
]
rows = "\n".join(f"<tr><td class='layer'>{esc(a)}</td><td class='tech'>{esc(b)}</td><td>{esc(c)}</td></tr>" for a, b, c in TECH)

page = f"""<title>The Fourth Mind Architecture</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700;800&family=Roboto:wght@400;500;700&family=Roboto+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>
  :root{{ color-scheme: light;
    --orange:#ff8702; --orange-dark:#c25f00; --orange-bg:#fff3e6;
    --blue:#1e3a8a; --blue-bg:#e8effc; --ink:#16203a; --muted:#5b6677; --line:#e4e9f2; --soft:#f6f8fc;
    --red:#b91c1c; }}
  *{{box-sizing:border-box;margin:0;padding:0;}}
  body{{background:#ffffff;color:var(--ink);font-family:Roboto,system-ui,sans-serif;line-height:1.55;
       padding-inline:max(16px,3vw);padding-block:36px 56px;-webkit-font-smoothing:antialiased;}}
  .wrap{{max-width:1680px;margin:0 auto;display:flex;flex-direction:column;gap:28px;}}
  header{{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:flex-end;gap:16px 40px;
         padding-bottom:22px;border-bottom:2px solid var(--line);}}
  .eyebrow{{font-family:'Roboto Mono',monospace;font-size:11.5px;font-weight:700;letter-spacing:.16em;
           text-transform:uppercase;color:var(--orange-dark);margin-bottom:8px;}}
  h1{{font-family:Montserrat,sans-serif;font-weight:800;font-size:clamp(26px,3vw,38px);line-height:1.12;
      letter-spacing:-.02em;text-wrap:balance;}}
  h1 span{{color:var(--orange);}}
  .lede{{max-width:62ch;color:var(--muted);font-size:15px;margin-top:10px;}}
  .stats{{display:flex;gap:28px;flex-wrap:wrap;}}
  .stat b{{display:block;font-family:Montserrat,sans-serif;font-size:26px;font-weight:800;color:var(--blue);
          font-variant-numeric:tabular-nums;line-height:1.1;}}
  .stat span{{font-family:'Roboto Mono',monospace;font-size:10.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);}}
  figure{{border:1px solid var(--line);border-radius:18px;background:#fff;overflow:hidden;}}
  .scroll{{overflow-x:auto;}}
  .scroll svg{{display:block;width:100%;min-width:1080px;height:auto;}}
  figcaption{{display:flex;flex-wrap:wrap;gap:10px 26px;align-items:center;padding:14px 22px;border-top:1px solid var(--line);
             background:var(--soft);font-size:12.5px;color:var(--muted);}}
  .key{{display:inline-flex;align-items:center;gap:8px;}}
  .key i{{display:inline-block;width:30px;height:0;border-top:2px solid var(--muted);}}
  .key i.or{{border-top:2px dashed var(--orange);}} .key i.bl{{border-color:var(--blue);}}
  .key i.red{{border-top:2px dashed var(--red);}}
  .cap{{flex-basis:100%;color:var(--ink);font-size:13px;}}
  h2{{font-family:Montserrat,sans-serif;font-size:20px;font-weight:800;display:flex;align-items:center;gap:10px;}}
  h2::before{{content:"";width:4px;height:20px;border-radius:2px;background:var(--orange);}}
  .tbl{{overflow-x:auto;border:1px solid var(--line);border-radius:14px;}}
  table{{width:100%;border-collapse:collapse;font-size:13.5px;min-width:720px;}}
  th{{text-align:left;font-family:'Roboto Mono',monospace;font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;
     color:var(--muted);background:var(--soft);padding:12px 18px;border-bottom:1px solid var(--line);}}
  td{{padding:12px 18px;border-bottom:1px solid var(--line);vertical-align:top;color:var(--muted);}}
  tr:last-child td{{border-bottom:none;}}
  td.layer{{font-family:'Roboto Mono',monospace;font-size:11.5px;font-weight:700;color:var(--orange-dark);
           text-transform:uppercase;letter-spacing:.08em;white-space:nowrap;}}
  td.tech{{color:var(--ink);font-weight:500;}}
  .principles{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;}}
  .p{{padding:18px 20px;border-radius:14px;background:var(--soft);}}
  .p h3{{font-family:Montserrat,sans-serif;font-size:14.5px;font-weight:700;margin-bottom:6px;color:var(--blue);}}
  .p p{{font-size:13.5px;color:var(--muted);}}
</style>
<div class="wrap">
  <header>
    <div>
      <div class="eyebrow">Embitel Technologies · SDV PR &amp; Competitive Intelligence</div>
      <h1>The Fourth Mind <span>·</span> Solution Architecture</h1>
      <p class="lede">How public and internal sources become a human-approved competitive picture: evidence is fetched and source-tagged, reasoned over by a four-module Claude pipeline with approval gates, persisted as project knowledge, and published as live dashboards.</p>
    </div>
    <div class="stats">
      <div class="stat"><b>6</b><span>layers</span></div>
      <div class="stat"><b>4</b><span>modules</span></div>
      <div class="stat"><b>2</b><span>human gates</span></div>
      <div class="stat"><b>5</b><span>rivals tracked</span></div>
    </div>
  </header>

  <figure>
    <div class="scroll">{svg}</div>
    <figcaption>
      <span class="key"><i></i>data flow</span>
      <span class="key"><i class="or"></i>human approval</span>
      <span class="key"><i class="bl"></i>persistence read / write</span>
      <span class="key"><i class="red"></i>blocked path (rerouted)</span>
      <span class="cap">Every claim enters the core with a provenance tag; modules 2 and 3 cannot start until the reviewer clears the gate before them.</span>
    </figcaption>
  </figure>

  <section style="display:flex;flex-direction:column;gap:14px;">
    <h2>Technology stack</h2>
    <div class="tbl"><table>
      <thead><tr><th>Layer</th><th>Technology</th><th>Role in the solution</th></tr></thead>
      <tbody>{rows}</tbody>
    </table></div>
  </section>

  <section style="display:flex;flex-direction:column;gap:14px;">
    <h2>Design principles</h2>
    <div class="principles">
      <div class="p"><h3>Human-gated, not autonomous</h3><p>Company Understanding and the competitor list each need explicit sign-off before downstream analysis runs, so strategy is built on facts the PR team has confirmed.</p></div>
      <div class="p"><h3>Provenance on every claim</h3><p>Each fact is tagged REPOSITORY, BROWSED, SYNOPSIS or TITLE-ONLY. Unreachable pages are flagged as gaps rather than filled with guesses.</p></div>
      <div class="p"><h3>Resilient retrieval</h3><p>When the egress proxy blocked WebSearch, news research was rerouted through Bing News via WebFetch, with each article verified directly.</p></div>
      <div class="p"><h3>Zero-dependency delivery</h3><p>Dashboards are plain HTML, CSS and JS with inlined imagery, so they load on any device and keep one stable, versioned link.</p></div>
    </div>
  </section>
</div>
"""

if __name__ == "__main__":
    import sys
    out_path = sys.argv[1] if len(sys.argv) > 1 else "architecture.html"
    doc = ('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n'
           '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
           + page.split("<div class=\"wrap\">", 1)[0] + "</head>\n<body>\n<div class=\"wrap\">"
           + page.split("<div class=\"wrap\">", 1)[1] + "</body>\n</html>\n")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(doc)
    print("wrote", out_path, len(doc), "bytes")
