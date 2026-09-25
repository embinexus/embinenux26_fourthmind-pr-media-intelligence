# Patch history

These are the one-off scripts that applied the visual upgrade to the Module Hub. They are kept for audit, not for re-running: each one expected the intermediate file names used during development. The current source of truth is `src/module-hub/index.html`. Build it with `tools/build.py`.

| Script | Change |
|---|---|
| `01_m1_visual_redesign.py` | Company Understanding tab: hero banner, new title, icon snapshot cards, four-pillar radial diagram |
| `02_add_module_banners.py` | Hero banners on Competitor Radar, PR Intelligence and PR Analytics tabs |
| `03_restore_accelerators_section.py` | Restores "Named Proprietary Accelerators", which the redesign had dropped (found by `qa/section_diff.py`) |

Every script uses exact-match anchors guarded by `assert`, so a patch fails loudly instead of editing the wrong place.
