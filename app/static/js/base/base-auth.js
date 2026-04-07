const loginButton = document.querySelector('.auth-moudel_login_button');
const loginForm = document.querySelector('.auth-moudel_login_form');

// 函数：发送登录请求
export async function sendLoginRequest(event) {
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
        // 登录成功，隐藏登录按钮，显示登出按钮和用户名
        const result = await response.json();
        
        const headerLoginButton = document.querySelector('.header-moudel_login_button');
        const headerLogoutButton = document.querySelector('.header-moudel_logout_button');
        const headerUsername = document.querySelector('.header-moudel_username');

        headerLoginButton.classList.add('is-hidden');
        headerLogoutButton.classList.remove('is-hidden');
        headerUsername.textContent = result.username;
    }
}

// 事件监听：登录按钮点击
loginButton.addEventListener('click', sendLoginRequest);