import { hideElement, showElement } from "./utils.js";

const headerUsername = document.querySelector('.header-moudel_username');

// 函数：发送状态请求
async function sendStatusRequest() {
    const response = await fetch('/status', {
        method: 'GET'
    });

    const result = await response.json();

    if (response.ok) {
        // 根据状态显示或隐藏元素
        if (result.status === 'logged_in') {
            showElement(document.querySelector('.header-moudel_logout_button'));
            showElement(document.querySelector('.header-moudel_username'));
            hideElement(document.querySelector('.header-moudel_login_button'));
            headerUsername.textContent = result.username;
        } else {
            hideElement(document.querySelector('.header-moudel_logout_button'));
            hideElement(document.querySelector('.header-moudel_username'));
            showElement(document.querySelector('.header-moudel_login_button'));
            headerUsername.textContent = '';
        }
    }
}

// 页面加载时发送状态请求
document.addEventListener('DOMContentLoaded', sendStatusRequest);