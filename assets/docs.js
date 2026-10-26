(function () {
  'use strict';
  var root = document.documentElement;
  var themeButton = document.getElementById('theme-toggle');
  var themeKey = 'graiphic-studio-doc-theme';
  try { root.dataset.theme = localStorage.getItem(themeKey) === 'light' ? 'light' : 'dark'; } catch (_) {}
  function updateThemeLabel() {
    var next = root.dataset.theme === 'dark' ? 'Light' : 'Dark';
    themeButton.textContent = next;
    themeButton.title = 'Switch to ' + next.toLowerCase() + ' theme';
    themeButton.setAttribute('aria-label', themeButton.title);
  }
  updateThemeLabel();
  themeButton.addEventListener('click', function () {
    root.dataset.theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
    try { localStorage.setItem(themeKey, root.dataset.theme); } catch (_) {}
    updateThemeLabel();
  });
  var base = new URL('./', window.location.href.split('#')[0]);
  var catalog = [], families = [], searchEntries = [], catalogReady = false, searchFailed = false;
  var groupState = Object.create(null), navigationObserver;
  function fetchText(path) { return fetch(new URL(path, base)).then(function (r) { if (!r.ok) throw new Error('Documentation resource unavailable: ' + path); return r.text(); }); }
  function routeHref(path) { return '#/' + path.replace(/^\//, '').replace(/\.md$/, ''); }
  function normalize(value) { return String(value || '').normalize('NFKD').replace(/[\u0300-\u036f]/g, '').toLowerCase(); }
  function currentPath() { return window.location.hash.split('?')[0].replace(/^#\//, '').replace(/\.md$/, '') || 'docs/index'; }
  Promise.all([fetchText('docs/functions/catalog.json'), fetchText('_sidebar.md'), fetchText('assets/examples/index.v1.json').then(JSON.parse).catch(function () { return {examples:[]}; })]).then(function (resources) {
    var data = JSON.parse(resources[0]);
    families = data.families || [];
    catalog = (data.entries || []).map(function (entry) {
      return {id:entry.catalog_id, title:entry.title_en, titleFr:entry.title_fr, family:entry.family, familyId:entry.family_id, path:entry.route, description:entry.summary, aliases:entry.aliases || [], connectors:entry.connector_names || []};
    });
    searchEntries = catalog.slice();
    (resources[2].examples || []).forEach(function (entry) {
      searchEntries.push({id:entry.id, title:entry.title, family:'Example · ' + entry.family, path:'docs/examples/' + entry.id + '.md', description:entry.summary + ' ' + entry.description, aliases:entry.catalog_ids || [], connectors:[]});
    });
    var seen = new Set(searchEntries.map(function (entry) { return entry.path; }));
    var re = /\[([^\]]+)\]\((\/docs\/[^)]+\.md)\)/g, match;
    while ((match = re.exec(resources[1]))) {
      var path = match[2].slice(1);
      if (!seen.has(path)) { seen.add(path); searchEntries.push({title:match[1], path:path, family:'User guide'}); }
    }
    searchEntries.forEach(function (entry) { entry.searchText = normalize([entry.title, entry.titleFr, entry.id, entry.family, entry.description, (entry.aliases || []).join(' '), (entry.connectors || []).join(' ')].join(' ')); });
    catalogReady = true; refreshSearch(); updateReadingTools();
  }).catch(function () { searchFailed = true; refreshSearch(); });
  function refreshSearch() {
    var input = document.getElementById('docs-search-input'); if (!input) return;
    var list = document.getElementById('docs-search-results'), status = document.getElementById('docs-search-status');
    var terms = normalize(input.value).trim().split(/\s+/).filter(Boolean);
    list.replaceChildren();
    if (!terms.length) { status.textContent = ''; list.hidden = true; return; }
    list.hidden = false;
    if (!catalogReady) { status.textContent = searchFailed ? 'Search unavailable. Browse the sidebar or Functions index.' : 'Loading search index…'; return; }
    var query = terms.join(' ');
    var results = searchEntries.filter(function (entry) { return terms.every(function (term) { return entry.searchText.includes(term); }); });
    function score(entry) { var title = normalize(entry.title); return title === query ? 0 : title.startsWith(query) ? 1 : title.includes(query) ? 2 : 3; }
    results.sort(function (a, b) { return score(a) - score(b) || a.title.localeCompare(b.title); });
    status.textContent = results.length ? results.length + ' results' + (results.length > 40 ? ' · first 40 shown; refine your search' : '') : 'No matching function, example or guide.';
    results.slice(0, 40).forEach(function (entry) {
      var item = document.createElement('li'), link = document.createElement('a'), family = document.createElement('small');
      link.href = routeHref(entry.path); link.append(document.createTextNode(entry.title)); family.textContent = entry.family || 'Function reference'; link.append(family); item.append(link); list.append(item);
      link.addEventListener('click', function () { input.value = ''; refreshSearch(); if (innerWidth <= 768) document.body.classList.remove('close'); });
    });
  }
  function installNavigation() {
    var sidebar = document.querySelector('.sidebar'); if (!sidebar) return;
    if (!navigationObserver) {
      navigationObserver = new MutationObserver(installNavigation);
      navigationObserver.observe(sidebar, {childList:true, subtree:true});
    }
    if (!document.getElementById('docs-search-input')) {
      var search = document.createElement('div'); search.className = 'docs-search';
      search.innerHTML = '<label for="docs-search-input">Search functions, examples and guides</label><input id="docs-search-input" type="search" placeholder="Name, terminal, type…" autocomplete="off" aria-controls="docs-search-results"><div id="docs-search-status" class="search-status" role="status"></div><ul id="docs-search-results" class="search-results" hidden></ul>';
      sidebar.insertBefore(search, sidebar.querySelector('.sidebar-nav'));
      var input = search.querySelector('input'); input.addEventListener('input', refreshSearch);
      input.addEventListener('keydown', function (event) {
        if (event.key === 'Escape') { input.value = ''; refreshSearch(); }
        var first = search.querySelector('.search-results a');
        if (first && event.key === 'ArrowDown') { event.preventDefault(); first.focus(); }
        if (first && event.key === 'Enter') { event.preventDefault(); first.click(); }
      });
    }
    sidebar.querySelectorAll('.sidebar-nav > ul > li strong').forEach(function (title) {
      var children = title.closest('li').querySelector('ul'); if (!children) return;
      var key = title.textContent, button = document.createElement('button');
      button.type = 'button'; button.className = 'nav-group'; button.textContent = key; button.setAttribute('aria-label', key);
      var expanded = key in groupState ? groupState[key] : key === 'Workspace guides' || key === 'Functions reference';
      if (Array.from(children.querySelectorAll('a')).some(function (a) { return a.getAttribute('href').split('?')[0] === '#/' + currentPath(); })) expanded = true;
      button.setAttribute('aria-expanded', String(expanded)); children.hidden = !expanded;
      button.addEventListener('click', function () { expanded = !expanded; groupState[key] = expanded; button.setAttribute('aria-expanded', String(expanded)); children.hidden = !expanded; });
      title.replaceWith(button);
    });
  }
  function updateReadingTools() {
    var article = document.querySelector('.markdown-section'); if (!article) return;
    article.id = 'main'; article.tabIndex = -1;
    var old = article.querySelector('.breadcrumb'); if (old) old.remove();
    var breadcrumb = document.createElement('nav'); breadcrumb.className = 'breadcrumb'; breadcrumb.setAttribute('aria-label', 'Breadcrumb');
    var parts = [{title:'Documentation', path:'docs/index.md'}];
    var entry = catalog.find(function (item) { return item.path.replace(/\.md$/, '') === currentPath(); });
    if (currentPath().startsWith('docs/functions')) {
      parts.push({title:'Functions', path:'docs/functions/index.md'});
      var family = entry && families.find(function (item) { return item.id === entry.familyId; });
      if (family) parts.push({title:family.name, path:family.route});
    }
    if (currentPath().startsWith('docs/examples')) parts.push({title:'Examples', path:'docs/examples/index.md'});
    var heading = article.querySelector('h1');
    parts.forEach(function (part) { var a = document.createElement('a'); a.href = routeHref(part.path); a.textContent = part.title; breadcrumb.append(a, document.createTextNode(' / ')); });
    var label = document.createElement('span'); label.textContent = heading ? heading.textContent : 'User guide'; label.setAttribute('aria-current', 'page'); breadcrumb.append(label); article.prepend(breadcrumb);
    var toc = document.querySelector('.page-toc'); if (toc) toc.remove();
    var headings = article.querySelectorAll('h2');
    if (headings.length > 1) {
      toc = document.createElement('nav'); toc.className = 'page-toc'; toc.setAttribute('aria-label', 'On this page');
      var title = document.createElement('strong'); title.textContent = 'On this page'; toc.append(title);
      headings.forEach(function (h) { var anchor = h.querySelector('a'); if (!anchor) return; var link = document.createElement('a'); link.href = anchor.href; link.textContent = h.textContent; toc.append(link); });
      document.body.append(toc);
    }
  }
  window.$docsify = {
    name:'Graiphic Studio', repo:'Graiphic/Graiphic-Studio', homepage:'docs/index.md', loadSidebar:true, loadNavbar:true, auto2top:true, relativePath:true, subMaxLevel:0, maxLevel:3,
    alias:{'/.*/_sidebar.md':'/_sidebar.md', '/.*/_navbar.md':'/_navbar.md'},
    plugins:[function (hook) {
      hook.afterEach(function (html, next) { next(html.replace(/src="(?:[^"]*\/)?assets\//g, 'src="' + base.pathname + 'assets/').replace(/href="(?:[^"]*\/)?assets\/examples\//g, 'href="' + base.pathname + 'assets/examples/')); });
      hook.doneEach(function () { installNavigation(); updateReadingTools(); });
    }]
  };
}());
