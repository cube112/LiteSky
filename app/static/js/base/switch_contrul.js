import { showElement, hideElement, toggleElement, resetForm } from './utils.js';

const headerMoudelLoginButton = document.querySelector('.header-moudel_login_button');
const authMoudelCloseButton = document.querySelector('.auth-moudel_close_button');
const authMoudelSwitchButtonToRegister = document.getElementsByClassName('auth-moudel_switch_button')[0];
const authMoudelSwitchButtonToLogin = document.getElementsByClassName('auth-moudel_switch_button')[1];
const authMoudel = document.querySelector('.auth-moudel');
const authMoudelLoginForm = document.querySelector('.auth-moudel_login_form');
const authMoudelRegisterForm = document.querySelector('.auth-moudel_register_form');


headerMoudelLoginButton.addEventListener('click', () => {
    toggleElement(authMoudel);
});

authMoudelCloseButton.addEventListener('click', () => {
    hideElement(authMoudel);
    // 重置状态
    if (authMoudelLoginForm.classList.contains('is-hidden')) {
        showElement(authMoudelLoginForm);
        hideElement(authMoudelRegisterForm);
    }
    // 重置表单
    resetForm(authMoudelLoginForm);
    resetForm(authMoudelRegisterForm);
});

authMoudelSwitchButtonToRegister.addEventListener('click', () => {
    toggleElement(authMoudelLoginForm);
    toggleElement(authMoudelRegisterForm);
});

authMoudelSwitchButtonToLogin.addEventListener('click', () => {
    toggleElement(authMoudelLoginForm);
    toggleElement(authMoudelRegisterForm);
});