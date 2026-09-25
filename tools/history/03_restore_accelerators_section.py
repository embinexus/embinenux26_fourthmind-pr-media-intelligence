with open('hub_final.html', 'r', encoding='utf-8') as f:
    html = f.read()

missing_section = '''      <div class="section">
        <div class="section-head"><div class="bar"></div><div class="section-title">Named Proprietary Accelerators</div></div>
        <div class="grid grid-2">
          <div class="card">
            <span class="badge badge-orange">Flagship IP</span>
            <div class="card-title" style="margin-top:10px;">Telematics SDK</div>
            <p class="kv-body">Claimed 50% reduction in time-to-market via pre-built middleware for power management, location services, driver monitoring, and data logging.</p>
          </div>
          <div class="card">
            <span class="badge badge-orange">Flagship IP</span>
            <div class="card-title" style="margin-top:10px;">OTA/FOTA Accelerator</div>
            <p class="kv-body">AWS-based, Kubernetes/Kafka/Lambda microservices, A/B partition updates, automatic rollback, Uptane-ready security. Tested across 350+ scenarios and 10,000+ devices.</p>
          </div>
        </div>
      </div>

'''

anchor = '      <div class="section">\n        <div class="section-head"><div class="bar"></div><div class="section-title">Target Markets &amp; Differentiators</div></div>'
assert html.count(anchor) == 1, html.count(anchor)
html = html.replace(anchor, missing_section + anchor, 1)

with open('hub_final2.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("done", len(html))
