from flask import request, jsonify, redirect, url_for, render_template
from flask import session, g

from ...exts import db
from ...models import User
from ..services.auth_check import login_required
from . import bp

# 登录接口
@bp.route('/auth_login', methods=['POST'])
def auth_login():
    request_data = request.get_json()
    username = request_data.get('username')
    password = request_data.get('password')

    user = db.session.scalar(db.select(User).where(User.username == username))
    if user and user.password == password:
        session['user_id'] = user.id
        return jsonify({
            'message': '登录成功',
            'username': user.username
            })
    return jsonify({'message': '用户名或密码错误'}), 401


# 登出接口
@bp.route('/auth_logout', methods=['POST'])
def auth_logout():
    session.pop('user_id', None)
    return jsonify({
        'message': '登出成功',
        'url_for': url_for('index.index')
        })


# 登录页面
@bp.route('/login')
def login():
    return render_template('login.html')


@bp.route('/dashboard')
@login_required
def dashboard():
    username = g.user.username
    return render_template('dashboard.html', username=username)