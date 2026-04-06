const loginButton = document.querySelector('.auth-moudel_login_button');
const loginForm = document.querySelector('.auth-moudel_login_form');

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

    if (response.ok) {
        // 登录成功，重定向到仪表盘
        const result = await response.json();
        window.location.href = result.redirect;
    }
}

// 事件监听：登录按钮点击
loginButton.addEventListener('click', sendLoginRequest);