var form = document.getElementById('signup-form');
var password = document.getElementById('password');
var confirm_password = document.getElementById('confirm_password');
var passwordError = document.getElementById('passwordError');

form.addEventListener('submit', function(event) {
    if (password.value !== confirm_password.value) {
        passwordError.style.display = 'block';
        event.preventDefault();
    } else {
        passwordError.style.display = 'none';
    }
});
