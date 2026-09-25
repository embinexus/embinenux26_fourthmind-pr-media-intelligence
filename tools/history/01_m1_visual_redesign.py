import re

with open('/tmp/claude-0/-home-claude/151ae2c6-054f-5407-8d6a-2ccc3fa5567e/scratchpad/current_hub.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('/tmp/claude-0/-home-claude/151ae2c6-054f-5407-8d6a-2ccc3fa5567e/scratchpad/banner_b64.txt', 'r', encoding='utf-8') as f:
    banner_b64 = f.read().strip()

# ---------- 1. New CSS block (append before closing </style>) ----------
new_css = """
  /* ===== Module 1 redesign: hero banner, snapshot icons, pillar diagram ===== */
  .m1-hero{
    position:relative; width:100%; border-radius:16px; overflow:hidden;
    margin-bottom:28px; aspect-ratio:16/5; background:#0b1220;
  }
  .m1-hero img{
    width:100%; height:100%; object-fit:cover; display:block;
  }
  .m1-hero::after{
    content:""; position:absolute; inset:0;
    background:linear-gradient(100deg, rgba(11,15,26,0.72) 0%, rgba(11,15,26,0.28) 45%, rgba(11,15,26,0.05) 75%);
  }
  .m1-hero-text{
    position:absolute; left:32px; top:0; bottom:0; display:flex; flex-direction:column; justify-content:center;
    max-width:520px; z-index:2;
  }
  .m1-hero-eyebrow{
    font-family:'Roboto Mono',monospace; font-size:11px; font-weight:700; letter-spacing:.16em; text-transform:uppercase;
    color:var(--orange); margin-bottom:10px;
  }
  .m1-hero-text h2{
    color:#fff; font-size:26px; font-weight:800; line-height:1.2; letter-spacing:-0.01em; text-wrap:balance;
  }
  @media (max-width:700px){
    .m1-hero{aspect-ratio:16/9;}
    .m1-hero-text{left:20px; max-width:88%;}
    .m1-hero-text h2{font-size:19px;}
  }

  /* Snapshot cards with icon badges */
  .snap-card{display:flex; gap:14px; align-items:flex-start;}
  .snap-icon{
    width:42px; height:42px; border-radius:11px; flex-shrink:0;
    display:flex; align-items:center; justify-content:center;
  }
  .snap-icon svg{width:22px; height:22px;}
  .snap-body{min-width:0;}

  /* Four Pillars diagram */
  .pillars-wrap{position:relative;}
  .pillars-diagram{
    position:relative; width:100%; min-height:460px;
    display:grid; grid-template-columns:1fr 1fr; grid-template-rows:1fr 1fr;
    gap:20px; align-items:stretch;
  }
  .pillars-diagram svg.connectors{
    position:absolute; inset:0; width:100%; height:100%; z-index:0; pointer-events:none;
  }
  .pillar-center{
    position:absolute; top:50%; left:50%; transform:translate(-50%,-50%);
    width:150px; height:150px; z-index:1; display:flex; align-items:center; justify-content:center;
  }
  .pillar-card{
    position:relative; z-index:2; background:#fff; border:1px solid var(--line); border-radius:14px;
    padding:20px 22px; display:flex; gap:14px; align-items:flex-start;
    box-shadow:0 2px 10px rgba(22,32,58,0.04);
  }
  .pillar-card:hover{border-color:var(--orange); box-shadow:0 8px 24px rgba(255,135,2,0.12);}
  .pillar-icon{
    width:46px; height:46px; border-radius:50%; flex-shrink:0;
    display:flex; align-items:center; justify-content:center;
    box-shadow:0 0 0 5px rgba(255,255,255,1), 0 2px 8px rgba(0,0,0,0.15);
  }
  .pillar-icon svg{width:24px; height:24px;}
  .pillar-title{font-weight:700; font-size:14.5px; color:var(--ink); margin-bottom:4px; line-height:1.3;}
  .pillar-body{font-size:12.5px; color:#4a5568; line-height:1.5;}

  @media (max-width:820px){
    .pillars-diagram{
      grid-template-columns:1fr; grid-template-rows:none; min-height:0; gap:14px;
    }
    .pillars-diagram svg.connectors, .pillar-center{display:none;}
    .pillar-card{grid-column:1 / -1;}
  }
"""
html = html.replace("</style>", new_css + "</style>")

# ---------- 2. Insert hero banner right after the m1 section opens ----------
old_m1_open = '''    <section class="screen active" id="m1">
      <div class="screen-header">
        <div class="eyebrow">Module 01 · Company Understanding</div>
        <h1>Embitel's SDV Business, Verified</h1>'''

new_m1_open = '''    <section class="screen active" id="m1">
      <div class="m1-hero">
        <img src="data:image/jpeg;base64,__BANNER_B64__" alt="Software-defined vehicle on a connected highway, streaming data to the cloud">
        <div class="m1-hero-text">
          <div class="m1-hero-eyebrow">The Fourth Mind · SDV Intelligence</div>
          <h2>Engineering the software layer of the next-generation vehicle</h2>
        </div>
      </div>
      <div class="screen-header">
        <div class="eyebrow">Module 01 · Company Understanding</div>
        <h1>Inside Embitel's SDV Offerings</h1>'''

assert old_m1_open in html, "m1 open anchor not found"
html = html.replace(old_m1_open, new_m1_open)
html = html.replace("__BANNER_B64__", banner_b64)

# ---------- 3. Company Snapshot: add icon badges ----------
old_snapshot = '''      <div class="section">
        <div class="section-head"><div class="bar"></div><div class="section-title">Company Snapshot</div></div>
        <div class="grid grid-3">
          <div class="card"><div class="kv-label">Founded</div><div class="kv-body" style="font-size:20px;font-weight:700;color:var(--ink);">2006</div></div>
          <div class="card"><div class="kv-label">Headquarters</div><div class="kv-body" style="font-size:20px;font-weight:700;color:var(--ink);">Bangalore, India</div></div>
          <div class="card"><div class="kv-label">Employees (overall)</div><div class="kv-body" style="font-size:20px;font-weight:700;color:var(--ink);">1,700+</div></div>
          <div class="card"><div class="kv-label">CARIAD India headcount</div><div class="kv-body" style="font-size:20px;font-weight:700;color:var(--ink);">1,000+</div></div>
          <div class="card"><div class="kv-label">Parent</div><div class="kv-body" style="font-size:16px;font-weight:700;color:var(--ink);">100% Volkswagen Group subsidiary</div></div>
          <div class="card"><div class="kv-label">Vision 2030</div><div class="kv-body" style="font-size:16px;font-weight:700;color:var(--ink);">4,000 employees · €250M turnover</div></div>
        </div>
      </div>'''

new_snapshot = '''      <div class="section">
        <div class="section-head"><div class="bar"></div><div class="section-title">Company Snapshot</div></div>
        <div class="grid grid-3">
          <div class="card snap-card">
            <div class="snap-icon" style="background:var(--orange-bg);">
              <svg viewBox="0 0 24 24" fill="none" stroke="var(--orange-dark)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="16" rx="2.5"/><line x1="3" y1="10" x2="21" y2="10"/><line x1="8" y1="2.5" x2="8" y2="6.5"/><line x1="16" y1="2.5" x2="16" y2="6.5"/></svg>
            </div>
            <div class="snap-body"><div class="kv-label">Founded</div><div class="kv-body" style="font-size:20px;font-weight:700;color:var(--ink);">2006</div></div>
          </div>
          <div class="card snap-card">
            <div class="snap-icon" style="background:var(--blue-bg);">
              <svg viewBox="0 0 24 24" fill="none" stroke="var(--blue)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s-7-6.2-7-11.2A7 7 0 0 1 19 9.8C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.3"/></svg>
            </div>
            <div class="snap-body"><div class="kv-label">Headquarters</div><div class="kv-body" style="font-size:20px;font-weight:700;color:var(--ink);">Bangalore, India</div></div>
          </div>
          <div class="card snap-card">
            <div class="snap-icon" style="background:var(--success-bg);">
              <svg viewBox="0 0 24 24" fill="none" stroke="var(--success)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="8" r="3"/><path d="M2.5 20c0-3.6 2.9-6 6.5-6s6.5 2.4 6.5 6"/><circle cx="17" cy="8.5" r="2.4"/><path d="M15.5 14.3c2.7.3 5 2.5 5 5.7"/></svg>
            </div>
            <div class="snap-body"><div class="kv-label">Employees (overall)</div><div class="kv-body" style="font-size:20px;font-weight:700;color:var(--ink);">1,700+</div></div>
          </div>
          <div class="card snap-card">
            <div class="snap-icon" style="background:#f3e8fd;">
              <svg viewBox="0 0 24 24" fill="none" stroke="#7c3aed" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 21V8l6-4 6 4v13"/><path d="M4 21h16"/><line x1="10" y1="12" x2="10" y2="12.01"/><line x1="14" y1="12" x2="14" y2="12.01"/><line x1="10" y1="16" x2="10" y2="16.01"/><line x1="14" y1="16" x2="14" y2="16.01"/></svg>
            </div>
            <div class="snap-body"><div class="kv-label">CARIAD India headcount</div><div class="kv-body" style="font-size:20px;font-weight:700;color:var(--ink);">1,000+</div></div>
          </div>
          <div class="card snap-card">
            <div class="snap-icon" style="background:#fde8e8;">
              <svg viewBox="0 0 24 24" fill="none" stroke="#c0392b" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2.5l7.5 3.2v6.1c0 4.8-3.2 8.3-7.5 9.7-4.3-1.4-7.5-4.9-7.5-9.7V5.7L12 2.5z"/><path d="M9 12l2 2 4-4.2"/></svg>
            </div>
            <div class="snap-body"><div class="kv-label">Parent</div><div class="kv-body" style="font-size:16px;font-weight:700;color:var(--ink);">100% Volkswagen Group subsidiary</div></div>
          </div>
          <div class="card snap-card">
            <div class="snap-icon" style="background:#e6f7f5;">
              <svg viewBox="0 0 24 24" fill="none" stroke="#0f9d8f" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4.6"/><circle cx="12" cy="12" r="0.9" fill="#0f9d8f"/></svg>
            </div>
            <div class="snap-body"><div class="kv-label">Vision 2030</div><div class="kv-body" style="font-size:16px;font-weight:700;color:var(--ink);">4,000 employees · €250M turnover</div></div>
          </div>
        </div>
      </div>'''

assert old_snapshot in html, "snapshot block not found"
html = html.replace(old_snapshot, new_snapshot)

# ---------- 4. Four Pillars: replace with radial diagram ----------
old_pillars = '''      <div class="section">
        <div class="section-head"><div class="bar"></div><div class="section-title">SDV Offerings — Four Pillars</div></div>
        <div class="grid grid-2">
          <div class="card">
            <div class="card-title">Vehicle Software Platforms &amp; Middleware</div>
            <p class="kv-body">AUTOSAR (MCAL/RTE/complex drivers), board support packages, Android Automotive &amp; Linux porting, Telematics SDK, diagnostics/comms stacks (UDS, DoIP, J1939, CAN/CAN FD), flash bootloader/ECU reprogramming.</p>
          </div>
          <div class="card">
            <div class="card-title">In-Vehicle Experience</div>
            <p class="kv-body">Infotainment (dual-display, gesture-controlled HUDs), digital instrument clusters, HMI/UI development, in-vehicle personalization, ADAS &amp; driver monitoring system validation.</p>
          </div>
          <div class="card">
            <div class="card-title">Electrification (EV)</div>
            <p class="kv-body">EV development, motor control for drivetrains, traction inverters &amp; DC-DC converters, battery management systems, on-board charger software, EV charging network solutions.</p>
          </div>
          <div class="card">
            <div class="card-title">Safety, Security &amp; Compliance</div>
            <p class="kv-body">ISO 26262 (ASIL D) software/hardware, functional safety analysis (FMEA/FMEDA), automotive cybersecurity (ISO/SAE 21434, UN R155), trusted apps, PKI, penetration testing.</p>
          </div>
        </div>
      </div>'''

new_pillars = '''      <div class="section">
        <div class="section-head"><div class="bar"></div><div class="section-title">SDV Offerings — Four Pillars</div></div>
        <p class="kv-body" style="margin-bottom:20px; max-width:640px;">End-to-end capabilities for the next generation of mobility — organized around the vehicle itself.</p>
        <div class="pillars-wrap">
          <div class="pillars-diagram">
            <svg class="connectors" viewBox="0 0 100 100" preserveAspectRatio="none">
              <line x1="50" y1="50" x2="27" y2="24" stroke="var(--blue)" stroke-width="0.4" stroke-dasharray="1.5,1.5"/>
              <line x1="50" y1="50" x2="73" y2="24" stroke="var(--orange)" stroke-width="0.4" stroke-dasharray="1.5,1.5"/>
              <line x1="50" y1="50" x2="27" y2="76" stroke="#15803d" stroke-width="0.4" stroke-dasharray="1.5,1.5"/>
              <line x1="50" y1="50" x2="73" y2="76" stroke="#7c3aed" stroke-width="0.4" stroke-dasharray="1.5,1.5"/>
            </svg>
            <div class="pillar-center" aria-hidden="true">
              <svg viewBox="0 0 150 150" width="150" height="150">
                <defs>
                  <radialGradient id="carGlow" cx="50%" cy="50%" r="55%">
                    <stop offset="0%" stop-color="#3b82f6" stop-opacity="0.55"/>
                    <stop offset="100%" stop-color="#3b82f6" stop-opacity="0"/>
                  </radialGradient>
                  <linearGradient id="carBody" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="0%" stop-color="#2b3648"/>
                    <stop offset="100%" stop-color="#141b26"/>
                  </linearGradient>
                </defs>
                <circle cx="75" cy="75" r="66" fill="url(#carGlow)"/>
                <g transform="translate(75,75) rotate(0)">
                  <rect x="-26" y="-58" width="52" height="116" rx="24" fill="url(#carBody)" stroke="#0b0f16" stroke-width="1"/>
                  <rect x="-17" y="-40" width="34" height="30" rx="9" fill="#0b0f16"/>
                  <rect x="-15" y="-38" width="30" height="10" rx="4" fill="#3b82f6" opacity="0.85"/>
                  <line x1="0" y1="-46" x2="0" y2="46" stroke="#3b82f6" stroke-width="2" opacity="0.9"/>
                  <circle cx="0" cy="0" r="3.2" fill="#3b82f6"/>
                  <rect x="-30" y="-30" width="4" height="16" rx="2" fill="#0b0f16"/>
                  <rect x="26" y="-30" width="4" height="16" rx="2" fill="#0b0f16"/>
                  <rect x="-30" y="16" width="4" height="16" rx="2" fill="#0b0f16"/>
                  <rect x="26" y="16" width="4" height="16" rx="2" fill="#0b0f16"/>
                </g>
              </svg>
            </div>

            <div class="pillar-card" style="grid-column:1; grid-row:1; align-self:start; justify-self:start; margin-top:0;">
              <div class="pillar-icon" style="background:var(--blue);">
                <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l8 4-8 4-8-4 8-4z"/><path d="M4 11l8 4 8-4"/><path d="M4 15l8 4 8-4"/></svg>
              </div>
              <div>
                <div class="pillar-title">Vehicle Software Platforms &amp; Middleware</div>
                <div class="pillar-body">AUTOSAR, board support packages, Android Automotive, Linux porting, Telematics SDK, diagnostics/comms stacks, flash bootloader/ECU reprogramming.</div>
              </div>
            </div>

            <div class="pillar-card" style="grid-column:2; grid-row:1; align-self:start; justify-self:end;">
              <div class="pillar-icon" style="background:var(--orange);">
                <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="1.4" fill="#fff"/><line x1="12" y1="7" x2="12" y2="8.6"/><line x1="12" y1="15.4" x2="12" y2="17"/><line x1="7" y1="12" x2="8.6" y2="12"/><line x1="15.4" y1="12" x2="17" y2="12"/></svg>
              </div>
              <div>
                <div class="pillar-title">In-Vehicle Experience</div>
                <div class="pillar-body">Infotainment, digital instrument clusters, HMI/UI development, in-vehicle personalization, ADAS &amp; driver monitoring system validation.</div>
              </div>
            </div>

            <div class="pillar-card" style="grid-column:1; grid-row:2; align-self:end; justify-self:start;">
              <div class="pillar-icon" style="background:#15803d;">
                <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 4 14h6l-1 8 9-12h-6l1-8z"/></svg>
              </div>
              <div>
                <div class="pillar-title">Electrification (EV)</div>
                <div class="pillar-body">EV development, motor control for drivetrains, traction inverters &amp; DC-DC converters, battery management systems, on-board charger software, EV charging network solutions.</div>
              </div>
            </div>

            <div class="pillar-card" style="grid-column:2; grid-row:2; align-self:end; justify-self:end;">
              <div class="pillar-icon" style="background:#7c3aed;">
                <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2.5l7.5 3.2v6.1c0 4.8-3.2 8.3-7.5 9.7-4.3-1.4-7.5-4.9-7.5-9.7V5.7L12 2.5z"/><path d="M9 12l2 2 4-4.2"/></svg>
              </div>
              <div>
                <div class="pillar-title">Safety, Security &amp; Compliance</div>
                <div class="pillar-body">ISO 26262 (ASIL D), functional safety analysis (FMEA/FMEDA), automotive cybersecurity (ISO/SAE 21434, UN R155), trusted apps, PKI, penetration testing.</div>
              </div>
            </div>
          </div>
        </div>
      </div>'''

assert old_pillars in html, "pillars block not found"
html = html.replace(old_pillars, new_pillars)

with open('/tmp/claude-0/-home-claude/151ae2c6-054f-5407-8d6a-2ccc3fa5567e/scratchpad/hub_v2_preview.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("OK, wrote", len(html), "bytes")
