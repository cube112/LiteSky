from flask import render_template, url_for, request, redirect, session

from ...exts import db
from ...models import User
from . import bp

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/login', methods=['POST'])
def login():
    form_data = request.form
    username = form_data.get('username')
    password = form_data.get('password')

    user = db.session.query(User).filter_by(username=username).first()
    if user and user.password == password:
        # 登录成功，保存用户信息到会话
        session['username'] = user.username
        # 重定向到用户的仪表盘
        return redirect(url_for('dashboard.dashboard'))
    else:
        # 登录失败，返回登录页面并显示错误信息
        return {
            'error': '用户名或密码错误'
        }