import { hideElement } from './utils.js';

const loginButton = document.querySelector('.auth-moudel_login_button');
const loginForm = document.querySelector('.auth-moudel_login_form');

const headerLoginButton = document.querySelector('.header-moudel_login_button');
const headerLogoutButton = document.querySelector('.header-moudel_logout_button');
const headerUsername = document.querySelector('.header-moudel_username');


// 函数：发送登录请求
async function sendLoginRequest(event) {
    event.preventDefault(); // 阻止默认表单提交行为

    const formData = new FormData(loginForm);
    const username = formData.get('username');
    const password = formData.get('password');

    const response = await fetch('/auth_login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'username': username,
            'password': password
        })
    });

    const result = await response.json();

    if (response.ok) {
        // 登录成功，隐藏登录按钮，显示登出按钮和用户名
        

        headerLoginButton.classList.add('is-hidden');
        headerLogoutButton.classList.remove('is-hidden');
        headerUsername.textContent = result.username;

        // 隐藏登录模态框
        hideElement(document.querySelector('.auth-moudel'));
    }

    else {
        // 登录失败，显示错误消息
    
        alert(result.message);
    }
}

// 事件监听：登录按钮点击
loginButton.addEventListener('click', sendLoginRequest);


// 函数：发送登出请求
async function sendLogoutRequest() {
    const response = await fetch('/auth_logout', {
        method: 'POST'
    });

    const result = await response.json();

    if (response.ok) {
        // 登出成功，显示登录按钮，隐藏登出按钮和用户名
        headerLoginButton.classList.remove('is-hidden');
        headerLogoutButton.classList.add('is-hidden');
        headerUsername.textContent = '';

        // 可选：重定向到首页
        window.location.href = result.url_for;
    } else {
        // 登出失败，显示错误消息
        alert(result.message);
    }
}

// 事件监听：登出按钮点击
headerLogoutButton.addEventListener('click', sendLogoutRequest);