
  const navItems = document.querySelectorAll('.nav-item');
  const screens = document.querySelectorAll('.screen');
  navItems.forEach(item => {
    item.addEventListener('click', () => {
      const target = item.getAttribute('data-target');
      navItems.forEach(n => n.classList.remove('active'));
      screens.forEach(s => s.classList.remove('active'));
      item.classList.add('active');
      document.getElementById(target).classList.add('active');
      window.scrollTo(0,0);
    });
  });

  // Linked apps (Competitor Radar, PR Analytics Dashboard).
  // In the offline build, each app is embedded in this page as base64 inside
  // <script type="application/octet-stream" id="embed-<name>">, and its link is
  // pointed at a Blob URL, so the Hub works as a single file on any machine,
  // with no server and no Claude account. In src/ (development) no payload is
  // embedded and the relative link to ../<name>/index.html is used instead.
  document.querySelectorAll('a[data-embed]').forEach(link => {
    const payload = document.getElementById('embed-' + link.getAttribute('data-embed'));
    if (!payload) return;
    try {
      const bytes = Uint8Array.from(atob(payload.textContent.trim()), c => c.charCodeAt(0));
      link.href = URL.createObjectURL(new Blob([bytes], { type: 'text/html;charset=utf-8' }));
    } catch (err) {
      console.warn('Could not prepare embedded app', link.getAttribute('data-embed'), err);
    }
  });
