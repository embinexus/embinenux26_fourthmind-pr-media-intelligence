#!/usr/bin/env python3
"""Build The Fourth Mind front-ends into single-file pages under dist/.

Source layout (each app in src/<app>/):
    index.html   markup, referencing ./styles.css, ./app.js and ../../assets/...
    styles.css   the app's stylesheet
    app.js       the app's behaviour (optional)

The source folders open directly in a browser for development. The build
inlines the stylesheet, the script and every image (as a base64 data: URI) so
each page in dist/ is one self-contained file: it works offline, needs no
server, and satisfies hosts whose content-security policy blocks external files.

    python3 tools/build.py            # build everything into dist/
    python3 tools/build.py --check    # also fail if any local reference is left

Standard library only.
"""
import base64
import mimetypes
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC, DIST = ROOT / "src", ROOT / "dist"

CSS_LINK = re.compile(r'<link rel="stylesheet" href="(styles\.css)">')
JS_TAG = re.compile(r'<script src="(app\.js)"></script>')
IMG_REF = re.compile(r'(?<=src=")(\.\./\.\./assets/[^"]+)(?=")')
EMBED_ATTR = re.compile(r'data-embed="([a-z0-9-]+)"')


def read(path: Path) -> str:
    if not path.is_file():
        sys.exit(f"[build] missing file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def data_uri(path: Path) -> str:
    if not path.is_file():
        sys.exit(f"[build] missing asset: {path.relative_to(ROOT)}")
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}"


def build_app(app_dir: Path) -> str:
    html = read(app_dir / "index.html")
    html = CSS_LINK.sub(lambda m: "<style>" + read(app_dir / m.group(1)) + "</style>", html)
    html = JS_TAG.sub(lambda m: "<script>" + read(app_dir / m.group(1)) + "</script>", html)
    html = IMG_REF.sub(lambda m: data_uri((app_dir / m.group(1)).resolve()), html)
    return html


def main() -> None:
    check = "--check" in sys.argv
    if DIST.exists():
        shutil.rmtree(DIST)
    built = {p.name: build_app(p) for p in sorted(SRC.iterdir()) if (p / "index.html").is_file()}

    # Embed linked apps (data-embed="<name>") so a page works as one offline file.
    for name, html in built.items():
        wanted = [n for n in EMBED_ATTR.findall(html) if n in built and n != name]
        if wanted:
            blobs = "".join(
                f'<script type="application/octet-stream" id="embed-{n}">'
                f'{base64.b64encode(built[n].encode("utf-8")).decode()}</script>\n'
                for n in dict.fromkeys(wanted))
            idx = html.rindex("<script>")
            built[name] = html[:idx] + blobs + html[idx:]
            print(f"[build] {name}: embedded {', '.join(dict.fromkeys(wanted))}")

    for name, html in built.items():
        if check and (CSS_LINK.search(html) or JS_TAG.search(html) or IMG_REF.search(html)):
            sys.exit(f"[build] unresolved local reference in {name}")
        out = DIST / name / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding="utf-8")
        print(f"[build] dist/{name}/index.html  {len(html) / 1024:,.0f} KB")

    arch_out = DIST / "architecture" / "index.html"
    arch_out.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([sys.executable, str(ROOT / "tools/architecture/build_architecture.py"), str(arch_out)], check=True)


if __name__ == "__main__":
    main()
