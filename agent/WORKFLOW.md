# The Fourth Mind: Agent Workflow Specification

This is the operating spec the Claude agent follows to run The Fourth Mind. The "reasoning core" is not a server. It is Claude (Sonnet 5 / Opus 5.5) running in Cowork on the Claude Agent SDK, with this spec, the knowledge base in `knowledge/`, and the tool set listed below. Each module produces a durable document and, where useful, a dashboard. Modules 2 and 3 cannot start until a human reviewer approves the output of the module before them.

## Scope rules (apply to every module)

| Rule | Detail |
|---|---|
| SDV only | Only Embitel's Software-Defined Vehicle business is in scope. The Digital Transformation pillar (e-commerce, omnichannel) is excluded from all research and output. |
| Rival definition | Competitors are technology service and solution providers. OEMs and Tier-1s are customers, never competitors. |
| Ground truth | `knowledge/CLAUDE.md` is the only authoritative source for how Embitel understands itself. It is not supplemented with outside research about Embitel. |
| No fabrication | If a page cannot be retrieved, the claim is flagged as a gap. Gaps are never filled with plausible guesses. |
| Evidence per claim | Every factual claim carries a source URL and a provenance tag. |

## Provenance tags (ingestion)

| Tag | Meaning |
|---|---|
| `REPOSITORY` | Stated in the Embitel SDV Knowledge Repository supplied by Embitel. |
| `BROWSED` | Verified against the live page at research time. |
| `SYNOPSIS-RECOVERED` | Page body not retrievable (JS-rendered or paywalled). Content comes from its meta-description or visible excerpt. |
| `TITLE-ONLY` | Only the title or URL was visible. Treated as a weak signal only. |

## Evidence labels (analysis)

| Label | Meaning |
|---|---|
| `FACT` | Directly supported by a cited source. |
| `INSIGHT` | An interpretation drawn from several facts. |
| `OPPORTUNITY` | A strategic conclusion for Embitel. |

## Tools

| Tool | Use |
|---|---|
| DOCX text extraction (Python) | Turns the repository document into structured knowledge (`knowledge/CLAUDE.md`). |
| WebFetch | Fetches a page and returns clean text. It also recovers meta-descriptions when a page body is blocked. |
| WebSearch | Intended primary search. It was **blocked by the egress proxy (HTTP 403)** in this environment. |
| Bing News through WebFetch | The fallback search route. Every article it surfaces is then fetched and verified directly. |
| Claude Projects | Persists `CLAUDE.md` and each module's document across sessions. |
| Artifacts + `db` capability | Hosts the dashboards and stores the competitor list, validation status and activity log for the Competitor Radar. |

## Pipeline

### Module 1: Company Understanding
- **Input:** Embitel SDV Knowledge Repository (`data/EMBITEL_SDV_KNOWLEDGE_REPOSITORY.docx`) plus each link it lists.
- **Steps:**
  1. Extract the repository.
  2. Browse every linked page and tag each fact.
  3. Organise the result into offerings (four pillars), capabilities, technologies, target markets, differentiators and positioning.
  4. List open questions for the reviewer.
- **Output:** the "Module 1 Output" section of `knowledge/CLAUDE.md`, shown in the Module Hub's Company Understanding tab.
- **Gate 1:** the reviewer approves the Company Understanding or requests changes. Approved on 2026-09-15.

### Module 2: Competitor Radar
- **Input:** approved Company Understanding.
- **Steps:**
  1. Propose candidate rivals that meet the rival definition.
  2. Research each rival from its own site, plus one cross-check source.
  3. Score each rival's confidence as High, Medium or Low. The score reflects how strong and how recent the evidence is.
  4. For each rival, record the strong overlap with Embitel, where Embitel is differentiated, and where the rival is stronger.
- **Output:** `knowledge/module2-competitor-analysis.md` and the interactive Competitor Radar (`src/competitor-radar`). The reviewer can keep, remove, add or query rivals, and every change is logged.
- **Gate 2:** the reviewer approves the rival list. The first draft had three rivals. The reviewer asked for LTTS to be researched and the list expanded to five, and then approved it on 2026-09-15.

### Module 3: PR Intelligence
- **Input:** the approved rival list. Research window: September 2025 to September 2026.
- **Steps (for each rival):**
  - positioning;
  - top five narratives;
  - SDV topics;
  - media outlets;
  - executive visibility;
  - event presence;
  - content formats;
  - emerging narratives;
  - PR strengths and gaps;
  - a table of sourced examples.

  A cross-competitor read then covers:
  - narratives owned by most rivals versus by few;
  - emerging narratives;
  - crowded topics;
  - under-represented topics;
  - white-space opportunities.
- **Output:** `knowledge/module3-pr-intelligence.md`, shown in the Module Hub's PR Intelligence tab.

### Module 4: PR Analytics & Strategy
- **Input:** Module 3 findings.
- **Steps:**
  1. Build the media visibility matrix, the executive visibility tracker and the event presence table.
  2. Build the competitive positioning matrix.
  3. Write six white-space opportunities for Embitel, each with its caveat.
- **Output:** `knowledge/module4-pr-analytics-dashboard.md` and the PR Analytics Dashboard (`src/pr-analytics-dashboard`).

## Agent loop

`Plan → Retrieve → Verify → Synthesize → Render`. When the reviewer gives feedback, the loop runs again. A dashboard is published only after a screenshot review (`tools/qa/screenshot_tabs.js`). A visual redesign is published only after a content-regression check against the previous version (`tools/qa/section_diff.py`).

## Lessons captured during the build

- **Artifact `db` snapshots:** `DocumentSnapshot.data` is a method. Reading `d.data` as a property returns the function itself, and its `.name` is the string `"data"`. That is why every competitor name once rendered as "data". The fix is to call `d.data()`. Every dynamic field is also HTML-escaped and given a fallback value, so "undefined" can never render.
- **Visual-only changes must not drop content:** one redesign patch removed the "Named Proprietary Accelerators" section. `section_diff.py` now compares headings before every publish.
- **Ask for a screenshot when a bug report is vague.** The screenshot, not code review, is what pinpointed the `.data` bug.
