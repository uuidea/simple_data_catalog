(function () {
  const ul = document.querySelector('nav.nav-menu ul');

  // Create a new <li> element.
  const li = document.createElement('li');
  li.classList.add('nav-item');
  li.dataset.depth = "0"

  const backToHome = document.createElement('a');
  backToHome.href = '/';
  backToHome.classList.add('nav-link');
  backToHome.textContent = 'Startpagina';

  // Add `↰`.
  const backToHomeSymbol = document.createElement('span');
  backToHomeSymbol.classList.add('nav-symbol');
  backToHomeSymbol.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="16px" height="16px" viewBox="0 -6 24 24"><path d="M6.906.384a1.75 1.75 0 0 1 2.187 0l5.25 4.2c.415.332.657.835.657 1.367v7.019a1.75 1.75 0 0 1-1.75 1.75h-2.5a.75.75 0 0 1-.75-.75V8.72H6v5.25a.75.75 0 0 1-.75.75h-2.5A1.75 1.75 0 0 1 1 12.97V5.95c0-.531.242-1.034.657-1.366l5.249-4.2Z"/></svg>';
  // backToHomeSymbol.textContent = '⌂'

  li.appendChild(backToHomeSymbol)
  li.appendChild(backToHome)

  // Prepend it to the <ul>.
  ul.prepend(li);
})();
