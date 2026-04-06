const headerMoudelLoginButton = document.querySelector('.header-moudel_login_button');
const authMoudelCloseButton = document.querySelector('.auth-moudel_close_button');
const authMoudelSwitchButtonToRegister = document.getElementsByClassName('auth-moudel_switch_button')[0];
const authMoudelSwitchButtonToLogin = document.getElementsByClassName('auth-moudel_switch_button')[1];
const authMoudel = document.querySelector('.auth-moudel');
const authMoudelLoginForm = document.querySelector('.auth-moudel_login_form');
const authMoudelRegisterForm = document.querySelector('.auth-moudel_register_form');

headerMoudelLoginButton.addEventListener('click', () => {
    authMoudel.classList.toggle('is-hidden');
});

authMoudelCloseButton.addEventListener('click', () => {
    authMoudel.classList.add('is-hidden');
});

authMoudelSwitchButtonToRegister.addEventListener('click', () => {
    authMoudelLoginForm.classList.toggle('is-hidden');
    authMoudelRegisterForm.classList.toggle('is-hidden');
});

authMoudelSwitchButtonToLogin.addEventListener('click', () => {
    authMoudelLoginForm.classList.toggle('is-hidden');
    authMoudelRegisterForm.classList.toggle('is-hidden');
});