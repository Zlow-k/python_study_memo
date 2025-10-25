(function(){
  const btn = document.getElementById('themeToggle');
  const root = document.documentElement;
  const storageKey = 'week6-theme';

  function applyTheme(theme){
    if(theme === 'dark'){
      root.setAttribute('data-theme','dark');
      btn.textContent = '☀️';
    } else {
      root.removeAttribute('data-theme');
      btn.textContent = '🌙';
    }
  }

  // init from storage or system preference
  const saved = localStorage.getItem(storageKey);
  if(saved){
    applyTheme(saved);
  } else {
    const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    applyTheme(prefersDark ? 'dark' : 'light');
  }

  btn.addEventListener('click', function(){
    const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
    const next = isDark ? 'light' : 'dark';
    applyTheme(next);
    localStorage.setItem(storageKey, next);
  });
})();
