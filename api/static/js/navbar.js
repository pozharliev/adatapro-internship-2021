document.addEventListener('DOMContentLoaded', function () {
  let burger = document.querySelector('.burger');
  let navbar = document.querySelector('.navbar-menu');
  burger.addEventListener('click', () => {
    burger.classList.toggle('is-active');
    navbar.classList.toggle('is-active');
  });
});