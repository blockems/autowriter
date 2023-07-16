function userLoggedIn() {
    // Hide login button and show avatar when the user is logged in
    const loginButton = document.getElementById('loginButton');
    const avatar = document.getElementById('avatar');
    loginButton.style.display = 'none';
    avatar.style.display = 'block';
}
