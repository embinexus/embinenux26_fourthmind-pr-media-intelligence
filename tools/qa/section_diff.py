#!/usr/bin/env python3
"""Content-regression check: make sure a redesigned page kept every section.

Compares the section headings (and card titles) of each tab in a baseline
Module Hub against a candidate build. Visual changes are allowed; losing a
heading is not. This is the check that caught the dropped
"Named Proprietary Accelerators" section during the visual upgrade.

    python3 tools/qa/section_diff.py <baseline.html> <candidate.html>

Exit code 1 if anything present in the baseline is missing from the candidate.
"""
import re
import sys
from html import unescape

SCREEN = re.compile(r'<section class="screen[^"]*" id="(m\d)">(.*?)</section>', re.S)
HEADING = re.compile(r'class="(?:section-title|card-title|pillar-title)"[^>]*>(.*?)</div>', re.S)


def outline(path: str) -> dict:
    html = open(path, encoding="utf-8").read()
    tabs = {}
    for tab_id, body in SCREEN.findall(html):
        tabs[tab_id] = [unescape(re.sub(r"<[^>]+>", "", h)).strip() for h in HEADING.findall(body)]
    return tabs


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    base, cand = outline(sys.argv[1]), outline(sys.argv[2])
    missing = 0
    for tab, headings in base.items():
        have = set(cand.get(tab, []))
        lost = [h for h in headings if h not in have]
        status = "OK" if not lost else f"MISSING {len(lost)}"
        print(f"{tab}: {len(headings)} headings in baseline, {len(cand.get(tab, []))} in candidate — {status}")
        for h in lost:
            print(f"    - {h}")
        missing += len(lost)
    sys.exit(1 if missing else 0)


if __name__ == "__main__":
    main()
