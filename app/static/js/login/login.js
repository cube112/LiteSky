const loginButton = document.querySelector('#login-moudel_login_button');
const loginForm = document.querySelector('.login_form');

loginButton.addEventListener('click', async (event) => {
    event.preventDefault();

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
        // 登录成功，跳转到首页或其他页面
        window.location.href = '/';
    }
});