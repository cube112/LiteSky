from flask import request, jsonify, redirect, url_for, render_template
from flask import session, g
from functools import wraps

from ...exts import db
from ...models import User
from . import bp

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
            'redirect': url_for('auth.dashboard')
            })
    return jsonify({'message': '用户名或密码错误'}), 401


@bp.route('/login')
def login():
    return render_template('login.html')


def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view


@bp.route('/dashboard')
@login_required
def dashboard():
    username = g.user.username
    return render_template('dashboard.html', username=username)