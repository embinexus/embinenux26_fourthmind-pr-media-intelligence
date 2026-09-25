with open('hub_v2_preview.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('chess_b64.txt') as f:
    chess_b64 = f.read().strip()
with open('eye_b64.txt') as f:
    eye_b64 = f.read().strip()
with open('analytics_b64.txt') as f:
    analytics_b64 = f.read().strip()

# --- CSS: generic hero only (no section-icon / card-icon additions) ---
css_add = """
  /* Generic hero (reuses m1-hero visual language for m2/m3/m4) */
  .mod-hero{ position:relative; width:100%; border-radius:16px; overflow:hidden; margin-bottom:28px; aspect-ratio:16/5; background:#0b1220; }
  .mod-hero img{ width:100%; height:100%; object-fit:cover; display:block; }
  .mod-hero::after{ content:""; position:absolute; inset:0; background:linear-gradient(100deg, rgba(11,15,26,0.75) 0%, rgba(11,15,26,0.32) 45%, rgba(11,15,26,0.06) 75%); }
  .mod-hero-text{ position:absolute; left:32px; top:0; bottom:0; display:flex; flex-direction:column; justify-content:center; max-width:520px; z-index:2; }
  .mod-hero-eyebrow{ font-family:'Roboto Mono',monospace; font-size:11px; font-weight:700; letter-spacing:.16em; text-transform:uppercase; color:var(--orange); margin-bottom:10px; }
  .mod-hero-text h2{ color:#fff; font-size:26px; font-weight:800; line-height:1.2; letter-spacing:-0.01em; text-wrap:balance; }
  @media (max-width:700px){ .mod-hero{aspect-ratio:16/9;} .mod-hero-text{left:20px; max-width:88%;} .mod-hero-text h2{font-size:19px;} }
"""
marker = "</style>"
assert marker in html
html = html.replace(marker, css_add + marker, 1)

def hero_block(b64, eyebrow, headline):
    return (f'\n      <div class="mod-hero">\n'
            f'        <img src="data:image/jpeg;base64,{b64}" alt="">\n'
            f'        <div class="mod-hero-text">\n'
            f'          <div class="mod-hero-eyebrow">{eyebrow}</div>\n'
            f'          <h2>{headline}</h2>\n'
            f'        </div>\n'
            f'      </div>\n')

anchor_m2 = '    <section class="screen" id="m2">\n      <div class="screen-header">'
assert anchor_m2 in html
html = html.replace(
    anchor_m2,
    '    <section class="screen" id="m2">' + hero_block(chess_b64, "The Fourth Mind · Competitive Strategy", "Five Rivals, Mapped Move by Move") + '      <div class="screen-header">',
    1
)

anchor_m3 = '    <section class="screen" id="m3">\n      <div class="screen-header">'
assert anchor_m3 in html
html = html.replace(
    anchor_m3,
    '    <section class="screen" id="m3">' + hero_block(eye_b64, "The Fourth Mind · Media Intelligence", "Watching Every Signal Competitors Send") + '      <div class="screen-header">',
    1
)

anchor_m4 = '    <section class="screen" id="m4">\n      <div class="screen-header">'
assert anchor_m4 in html
html = html.replace(
    anchor_m4,
    '    <section class="screen" id="m4">' + hero_block(analytics_b64, "The Fourth Mind · PR Analytics", "Turning PR Noise Into a Strategic Map") + '      <div class="screen-header">',
    1
)

with open('hub_final.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("done", len(html))
