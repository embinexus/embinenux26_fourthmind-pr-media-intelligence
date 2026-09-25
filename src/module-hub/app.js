
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
