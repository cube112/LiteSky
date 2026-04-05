const headerLoginButton = document.querySelector('.header-login-button');
const loginContainer = document.querySelector('.login-register.is-hidden');

headerLoginButton.addEventListener('click', () => {
    loginContainer.classList.remove('is-hidden');
});
