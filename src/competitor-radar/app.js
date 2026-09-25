
(function(){
  "use strict";

  var SEED_COMPETITORS = [
    {
      id:"kpit", order:1, name:"KPIT Technologies", confidence:"High", status:"approved",
      capabilities:"Positions itself explicitly as \"a global partner to the automotive and Mobility ecosystem for making software-defined vehicles a reality.\" Covers E/E architecture evolution (distributed → domain-centralized → zonal/central-compute), ADAS & autonomous driving, EV and conventional powertrains, connected vehicles, AUTOSAR, and vehicle diagnostics.",
      overlap:"Near-total overlap on the technical stack — AUTOSAR, ADAS, EV powertrain software, connected vehicles/telematics, embedded engineering — and an identical “software-hardware decoupling” SDV narrative. Both are India-headquartered, pure-play automotive engineering services providers selling to OEMs/Tier-1s.",
      why:"Same buyer, same core service (turnkey embedded/software engineering), same explicit SDV positioning language — the closest like-for-like match to Embitel's stated business model.",
      evidence:"kpit.com (SDV positioning page) · en.wikipedia.org/wiki/KPIT_Technologies",
      strongOverlap:[{t:"fact",x:"AUTOSAR, ADAS, EV powertrain, connected vehicles, embedded engineering, explicit SDV narrative"}],
      differentiated:[{t:"interp",x:"VW Group ownership + CARIAD India access; KPIT is ~7–8× Embitel's headcount, so Embitel can offer more senior-attention / turnkey intimacy per program"}],
      stronger:[{t:"fact",x:"~13,000 employees, footprint across Europe/USA/Japan/China/Thailand/India, ~$610M revenue"},{t:"interp",x:"likely wins very large multi-year OEM programs on scale"}]
    },
    {
      id:"tata-elxsi", order:2, name:"Tata Elxsi", confidence:"High", status:"approved",
      capabilities:"Explicitly automotive-and-SDV-branded with named platforms: AVENIR (SDV product suite), TETHER AUTO (connected vehicle platform), DevStudio.ai (GenAI-assisted, ASPICE-aligned software engineering) and NEURON (autonomous network platform). Also covers cockpit/HMI design, cybersecurity and cloud.",
      overlap:"Strong overlap on cybersecurity, cloud/connected-vehicle software and cockpit/HMI work. Both explicitly use “software-defined vehicle” as self-positioning language and target OEMs directly.",
      why:"Directly competes for the same category of OEM SDV engineering and cockpit/connected-vehicle contracts, with its own named SDV product suite — a similar “accelerator/IP” strategy to Embitel's Telematics SDK and OTA/FOTA Accelerator.",
      evidence:"tataelxsi.com — industries/automotive and platforms sections",
      strongOverlap:[{t:"fact",x:"Cybersecurity, cockpit/HMI, connected-vehicle software, explicit SDV branding"}],
      differentiated:[{t:"interp",x:"VW Group pedigree, TISAX AL3 / ASPICE CL2 depth vs. Tata Elxsi's broader design/UX-led brand"}],
      stronger:[{t:"fact",x:"Named market-facing SDV suite (AVENIR) + public OEM partnership with JSW Motors"},{t:"interp",x:"arguably a stronger visible “SDV brand” than Embitel today"}]
    },
    {
      id:"sasken", order:3, name:"Sasken Technologies", confidence:"Medium", status:"approved",
      capabilities:"End-to-end product development across ADAS & autonomous driving, integrated cockpit/IVI, telematics & V2X (LTE-based), and body electronics/AUTOSAR (“Chip to Cognition”). Platforms: Android, Automotive Grade Linux, GENIVI Linux, QNX. ISO 26262 functional safety.",
      overlap:"Close overlap on ADAS, telematics, AUTOSAR and ISO 26262 functional safety. Also the closest match to Embitel in company scale (~2,000 employees vs. Embitel's 1,700+) — a more apples-to-apples competitor than the larger names above.",
      why:"Same customer base (OEMs/Tier-1s across North America, Europe, Japan), very similar technical service menu, comparable company size and positioning.",
      evidence:"sasken.com/industries/automotive · en.wikipedia.org/wiki/Sasken_Technologies (employee/revenue figures last updated ~2019 — dated)",
      strongOverlap:[{t:"fact",x:"ADAS, telematics, AUTOSAR, ISO 26262, comparable company scale"}],
      differentiated:[{t:"interp",x:"VW Group backing + AutoTech Awards 2026 win; Sasken's SDV claim looks less product/IP-backed than Embitel's own accelerators"}],
      stronger:[{t:"fact",x:"Longer, more diversified platform experience (Android/AGL/GENIVI/QNX) + existing Tier-1 JV with Tata Autocomp"},{t:"interp",x:"may signal a more mature cockpit/IVI practice specifically"}]
    },
    {
      id:"ltts", order:4, name:"L&T Technology Services", confidence:"High", status:"approved",
      capabilities:"Dedicated automotive page shows explicit SDV positioning: Vehicle Electrification, Autonomous Drive & ADAS, Connected Mobility, and a named “Software-Defined Vehicles” pillar. Five named accelerators: REFACTO (AUTOSAR automation), eVOLTTS (e-mobility), EDGYneer (edge management), SafeX (functional safety/CI-CD), AnnotAI (AI data annotation).",
      overlap:"Very close overlap — AUTOSAR, ADAS, EV, telematics, functional safety, cybersecurity — and a named-accelerator strategy that mirrors Embitel's own Telematics SDK / OTA Accelerator approach almost point-for-point.",
      why:"Serves “some of the largest auto manufacturers, OEMs, and Tier 1s” with the same turnkey SDV engineering model; recognized as a “Leader” by Everest Group and ISG in this exact category.",
      evidence:"ltts.com/industry/mobility/automotive — correction from an earlier pass that only checked the LTTS homepage",
      strongOverlap:[{t:"fact",x:"AUTOSAR, ADAS, EV, telematics, functional safety, cybersecurity, named-accelerator strategy"}],
      differentiated:[{t:"interp",x:"VW Group pedigree is a credibility asset LTTS, an independent public company, doesn't have"}],
      stronger:[{t:"fact",x:"Five named proprietary SDV accelerators, analyst “Leader” recognition, $1.24B revenue, 423 global clients"},{t:"interp",x:"the most direct match to Embitel's own accelerator-IP strategy, at far greater scale and market validation"}]
    },
    {
      id:"einfochips", order:5, name:"eInfochips (an Arrow Electronics company)", confidence:"Medium", status:"approved",
      capabilities:"End-to-end automotive hardware/firmware/software engineering: ADAS & autonomous vehicles, HEMS/EV charging, V2X, telematics, infotainment. AUTOSAR-compliant stack (BSW/RTE/COM), ISO 26262, cybersecurity, ASPICE v3.1, AUTOSAR consortium member.",
      overlap:"Near-total technical overlap — ADAS, EV/BMS, EV charging, V2X, AUTOSAR, ISO 26262, cybersecurity — plus a similar certification profile and identical target customers (global OEMs and Tier-1s).",
      why:"Same service category, same customers, same technical stack, explicit SDV self-positioning, dual India/US presence (Ahmedabad + San Jose) similar in spirit to Embitel's multi-geography model.",
      evidence:"einfochips.com/industries/automotive — no current employee/revenue figure found in fetched content (flagged as a data gap)",
      strongOverlap:[{t:"fact",x:"ADAS, EV/BMS, V2X, AUTOSAR, ISO 26262, cybersecurity, parent-company structure"}],
      differentiated:[{t:"interp",x:"Embitel's direct VW Group program access vs. eInfochips' Arrow Electronics (semiconductor-distribution) parentage — a different kind of backing"}],
      stronger:[{t:"fact",x:"Dual India/US presence, ASPICE v3.1 + AUTOSAR consortium membership, silicon-vendor partnerships (NXP, Infineon, Qualcomm, NVIDIA)"},{t:"interp",x:"may signal deeper hardware/chip-level integration relationships than Embitel has publicly shown"}]
    }
  ];

  var SEED_LOG = [
    {ts:"Sept 15", actor:"The Fourth Mind", detail:"Drafted 3 candidate competitors: KPIT, Tata Elxsi, Sasken — presented for review."},
    {ts:"Sept 15", actor:"Anne", detail:"Requested L&T Technology Services be researched, and the list expanded to 5."},
    {ts:"Sept 15", actor:"The Fourth Mind", detail:"Added LTTS (correcting an earlier, incomplete exclusion) and eInfochips; revised comparison table."},
    {ts:"Sept 15", actor:"Anne", detail:"Approved the list of 5 competitors."}
  ];

  var STATUS = {value:"approved", approvedBy:"Anne Chakraborti", approvedAt:"Sept 2026"};

  var els = {
    cards: document.getElementById("cards"),
    table: document.getElementById("compare-table"),
    log: document.getElementById("log"),
    approvalSummary: document.getElementById("approval-summary"),
    statusBanner: document.getElementById("status-banner"),
    statusTitle: document.getElementById("status-title"),
    statusMeta: document.getElementById("status-meta"),
    reopenBtn: document.getElementById("reopen-btn"),
    connState: document.getElementById("conn-state"),
    railStat: document.getElementById("rail-stage3-stat")
  };

  var state = {
    competitors: SEED_COMPETITORS.map(function(c){ return Object.assign({}, c); }),
    log: SEED_LOG.slice(),
    status: Object.assign({}, STATUS)
  };

  var db = null;

  function esc(s){
    return String(s == null ? "" : s).replace(/[&<>"']/g, function(c){
      return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c];
    });
  }

  // FIX: safe numeric/text fallback so a missing or malformed field can
  // never render the literal string "undefined" anywhere in the UI.
  function safeOrder(c, fallbackIndex){
    var n = c && c.order;
    if(typeof n === "number" && !isNaN(n)) return n;
    var parsed = parseInt(n, 10);
    if(!isNaN(parsed)) return parsed;
    return fallbackIndex + 1; // fall back to display position (1-based)
  }
  function safeText(v, fallback){
    if(v == null || v === "" ) return fallback || "";
    return v;
  }

  function confClass(c){ return c === "High" ? "high" : (c === "Medium" ? "medium" : "low"); }

  function tagLine(items){
    if(!Array.isArray(items) || !items.length) return '<span class="tag interp">read</span>Not yet researched.';
    return items.map(function(i){
      return '<span class="tag ' + (i.t === "fact" ? "fact" : "interp") + '">' + (i.t === "fact" ? "fact" : "read") + '</span>' + esc(i.x);
    }).join("<br><br>");
  }

  function render(){
    renderStatus();
    renderCards();
    renderTable();
    renderLog();
    renderApprovalSummary();
  }

  function renderStatus(){
    var approved = state.competitors.filter(function(c){ return c.status === "approved"; }).length;
    var total = state.competitors.length;
    var pending = state.status.value !== "approved";
    els.statusBanner.classList.toggle("pending", pending);
    if(pending){
      els.statusTitle.textContent = "Pending your review — " + approved + " of " + total + " kept";
      els.statusMeta.textContent = state.status.reason ? ("Reopened: " + state.status.reason) : "Awaiting approval before PR & Media Research can begin.";
      els.reopenBtn.textContent = "Mark approved";
      els.railStat.textContent = "In review";
    } else {
      els.statusTitle.textContent = "Approved — " + approved + " of " + total + " competitors confirmed";
      els.statusMeta.textContent = "Approved by " + esc(safeText(state.status.approvedBy, "Anne")) + " · Embitel Technologies India · " + esc(safeText(state.status.approvedAt, "Sept 2026"));
      els.reopenBtn.textContent = "Reopen for revision";
      els.railStat.textContent = "✓ Approved";
    }
  }

  function renderCards(){
    els.cards.innerHTML = state.competitors
      .slice()
      .sort(function(a,b){ return safeOrder(a,0) - safeOrder(b,0); })
      .map(function(c, idx){
        var removed = c.status === "removed";
        var orderNum = safeOrder(c, idx);
        return '' +
        '<div class="card' + (removed ? " removed" : "") + '" data-id="' + esc(c.id) + '">' +
          '<div class="top">' +
            '<div><span class="rank">#' + esc(orderNum) + '</span><h3>' + esc(safeText(c.name, "Unnamed competitor")) + '</h3></div>' +
            '<span class="pill ' + confClass(c.confidence) + '">' + esc(safeText(c.confidence, "Unrated")) + '</span>' +
          '</div>' +
          '<div class="field"><div class="k">Relevant SDV capabilities</div>' + esc(safeText(c.capabilities, "Not yet researched.")) + '</div>' +
          '<div class="field"><div class="k">Overlap with Embitel</div>' + esc(safeText(c.overlap, "Not yet researched.")) + '</div>' +
          '<div class="field"><div class="k">Why a competitor</div>' + esc(safeText(c.why, "Not yet researched.")) + '</div>' +
          '<div class="field"><div class="k">Evidence</div><div class="evidence">' + esc(safeText(c.evidence, "No evidence recorded yet.")) + '</div></div>' +
          '<div class="ctrl">' +
            (removed
              ? '<span class="removed-flag">✕ Removed</span><button class="btn small" data-action="keep" data-id="' + esc(c.id) + '">Restore</button>'
              : '<span class="kept-flag">✓ Kept</span><button class="btn ghost small" data-action="remove" data-id="' + esc(c.id) + '">Remove</button>') +
          '</div>' +
        '</div>';
      }).join("");
  }

  function renderTable(){
    var active = state.competitors.slice().sort(function(a,b){ return safeOrder(a,0) - safeOrder(b,0); });
    var head = '<tr><th>Signal</th>' + active.map(function(c){ return '<th>' + esc(safeText(c.name, "Unnamed competitor")) + '</th>'; }).join("") + '</tr>';
    function row(label, key){
      return '<tr><td class="rowlabel">' + esc(label) + '</td>' + active.map(function(c){
        return '<td>' + tagLine(c[key]) + '</td>';
      }).join("") + '</tr>';
    }
    els.table.innerHTML = head +
      row("Strong overlap", "strongOverlap") +
      row("Embitel differentiated", "differentiated") +
      row("Competitor stronger", "stronger");
  }

  function renderLog(){
    els.log.innerHTML = state.log.map(function(e){
      return '<div class="log-entry"><span class="time">' + esc(safeText(e.ts,"—")) + '</span><span><span class="actor">' + esc(safeText(e.actor,"Unknown")) + '</span> — <span class="detail">' + esc(safeText(e.detail,"")) + '</span></span></div>';
    }).join("");
  }

  function renderApprovalSummary(){
    var kept = state.competitors.filter(function(c){ return c.status === "approved"; });
    var removed = state.competitors.filter(function(c){ return c.status === "removed"; });
    var html = kept.length + " kept";
    if(removed.length) html += ", " + removed.length + " removed";
    html += ". Full write-up lives alongside the approved Company Understanding in The Fourth Mind knowledge base.";
    els.approvalSummary.textContent = html;
  }

  function addLog(actor, detail){
    state.log.push({ts:"just now", actor:actor, detail:detail});
    persistLog({ts: new Date().toISOString(), actor:actor, detail:detail});
  }

  // ---- persistence (db capability, graceful no-op if unavailable) ----
  function persistCompetitor(c){
    if(!db) return;
    db.doc("competitors/" + c.id).set(c).catch(function(){});
  }
  function persistStatus(){
    if(!db) return;
    db.doc("module2/status").set(state.status).catch(function(){});
  }
  function persistLog(entry){
    if(!db) return;
    db.doc("activityLog/" + Date.now() + "-" + Math.random().toString(36).slice(2,7)).set(entry).catch(function(){});
  }

  function setConnState(msg){ els.connState.textContent = msg; }

  // ---- interactions ----
  els.cards.addEventListener("click", function(e){
    var btn = e.target.closest("button[data-action]");
    if(!btn) return;
    var id = btn.getAttribute("data-id");
    var c = state.competitors.find(function(x){ return x.id === id; });
    if(!c) return;
    if(btn.getAttribute("data-action") === "remove"){
      c.status = "removed";
      addLog("You", "Removed " + c.name + " from the shortlist.");
    } else {
      c.status = "approved";
      addLog("You", "Restored " + c.name + " to the shortlist.");
    }
    persistCompetitor(c);
    render();
  });

  els.reopenBtn.addEventListener("click", function(){
    if(state.status.value === "approved"){
      state.status.value = "pending";
      state.status.reason = null;
      addLog("You", "Reopened the competitor list for revision.");
    } else {
      state.status.value = "approved";
      state.status.approvedBy = "Anne Chakraborti";
      state.status.approvedAt = new Date().toLocaleDateString("en-IN", {month:"short", year:"numeric"});
      addLog("You", "Re-approved the competitor list.");
    }
    persistStatus();
    render();
  });

  function wireForm(openBtnId, formId, closeSelector, submitId, onSubmit){
    var openBtn = document.getElementById(openBtnId);
    var form = document.getElementById(formId);
    openBtn.addEventListener("click", function(){ form.classList.add("open"); });
    form.querySelectorAll(closeSelector).forEach(function(b){
      b.addEventListener("click", function(){ form.classList.remove("open"); });
    });
    document.getElementById(submitId).addEventListener("click", onSubmit);
  }

  wireForm("add-btn", "add-form", "[data-close='add-form']", "add-submit", function(){
    var name = document.getElementById("add-name").value.trim();
    var note = document.getElementById("add-note").value.trim();
    if(!name) return;
    var id = "custom-" + Date.now();
    var c = {
      id:id, order: state.competitors.length + 1, name:name, confidence:"Low", status:"approved",
      capabilities: note || "Added manually — pending research.",
      overlap:"Not yet researched.", why:"Added by Anne for consideration.",
      evidence:"User-added — awaiting evidence from a live research pass.",
      strongOverlap:[{t:"interp", x:"Not yet researched."}],
      differentiated:[{t:"interp", x:"Not yet researched."}],
      stronger:[{t:"interp", x:"Not yet researched."}]
    };
    state.competitors.push(c);
    addLog("You", "Added " + name + " for consideration" + (note ? (": " + note) : "."));
    persistCompetitor(c);
    document.getElementById("add-name").value = "";
    document.getElementById("add-note").value = "";
    document.getElementById("add-form").classList.remove("open");
    render();
  });

  wireForm("feedback-btn", "feedback-form", "[data-close='feedback-form']", "feedback-submit", function(){
    var note = document.getElementById("feedback-note").value.trim();
    if(!note) return;
    addLog("You", "Feedback: " + note);
    document.getElementById("feedback-note").value = "";
    document.getElementById("feedback-form").classList.remove("open");
    render();
  });

  // ---- boot ----
  function boot(saved){
    if(saved && saved.competitors) state = saved;
    render();

    if(window.claude && window.claude.use){
      window.claude.use("db").then(function(handle){
        db = handle;
        if(!db){ setConnState("Viewing a local copy — changes here won't be saved for other viewers."); return; }
        setConnState("Connected — your changes are saved for everyone who opens this page.");

        db.collection("competitors").onSnapshot(function(snap){
          if(snap && snap.docs && snap.docs.length){
            // FIX: DocumentSnapshot.data is a METHOD, not a property.
            // Reading it as a property returns the function object itself
            // (whose intrinsic .name is the literal string "data") instead
            // of the document body — the root cause of names showing "data".
            state.competitors = snap.docs.map(function(d){ return d.data(); }).filter(Boolean).sort(function(a,b){ return safeOrder(a,0)-safeOrder(b,0); });
            render();
          } else {
            state.competitors.forEach(persistCompetitor);
          }
        });
        db.doc("module2/status").onSnapshot(function(doc){
          if(doc && doc.exists){
            state.status = doc.data() || state.status;
            render();
          } else {
            persistStatus();
          }
        });
        db.collection("activityLog").orderBy("ts","asc").onSnapshot(function(snap){
          if(snap && snap.docs && snap.docs.length > SEED_LOG.length){
            state.log = snap.docs.map(function(d){
              var v = d.data() || {};
              var ts = v.ts ? new Date(v.ts) : null;
              return {ts: (ts && !isNaN(ts.getTime())) ? ts.toLocaleTimeString("en-IN",{hour:"2-digit",minute:"2-digit"}) : "—", actor:v.actor, detail:v.detail};
            });
            render();
          }
        });
      }).catch(function(){ setConnState("Viewing a local copy — changes here won't be saved for other viewers."); });
    } else {
      setConnState("Viewing a local copy — changes here won't be saved for other viewers.");
    }
  }

  if(window.claude && window.claude.hot && window.claude.hot.snapshot){
    window.claude.hot.snapshot(function(){ return state; });
  }
  if(window.claude && window.claude.hot && window.claude.hot.ready){
    window.claude.hot.ready(boot);
  } else {
    boot(window.claude && window.claude.hot ? window.claude.hot.data : null);
  }
})();
