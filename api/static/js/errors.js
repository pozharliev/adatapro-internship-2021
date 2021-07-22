const error = document.querySelectorAll('.errorlist li');

error.forEach(error => {
    error.classList.add('notification', 'is-danger');
});