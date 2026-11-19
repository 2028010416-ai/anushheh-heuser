const greetingButton = document.querySelector('#greeting-button');
const greeting = document.querySelector('#greeting');
const status = document.querySelector('#status');
const year = document.querySelector('#year');

year.textContent = `© ${new Date().getFullYear()}`;

greetingButton.addEventListener('click', () => {
  greeting.textContent = 'Hello! This Homework 6 website is ready to publish.';
  status.textContent = 'Deployed';
});
