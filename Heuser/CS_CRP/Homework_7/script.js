const checkButton = document.querySelector('#check-button');
const result = document.querySelector('#result');
const year = document.querySelector('#year');

year.textContent = `© ${new Date().getFullYear()}`;

checkButton.addEventListener('click', () => {
  result.textContent = 'Project files are ready. GitHub Pages can now publish this site.';
});
