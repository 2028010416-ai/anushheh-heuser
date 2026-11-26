const menuToggle = document.querySelector('#menu-toggle');
const mainNav = document.querySelector('#main-nav');
const journeyButton = document.querySelector('#journey-button');
const journeyMessage = document.querySelector('#journey-message');
const year = document.querySelector('#year');

year.textContent = new Date().getFullYear();

menuToggle.addEventListener('click', () => {
  const isOpen = mainNav.classList.toggle('open');
  menuToggle.setAttribute('aria-expanded', String(isOpen));
  menuToggle.setAttribute('aria-label', isOpen ? 'Close navigation' : 'Open navigation');
});

mainNav.querySelectorAll('a').forEach((link) => {
  link.addEventListener('click', () => {
    mainNav.classList.remove('open');
    menuToggle.setAttribute('aria-expanded', 'false');
    menuToggle.setAttribute('aria-label', 'Open navigation');
  });
});

journeyButton.addEventListener('click', () => {
  journeyMessage.textContent = 'Your story in Asterfall begins now. Choose a realm above to explore.';
  document.querySelector('#kingdom').scrollIntoView({ behavior: 'smooth' });
});
