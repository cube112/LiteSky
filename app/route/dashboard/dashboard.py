from flask import render_template, session, redirect, url_for
from functools import wraps

from . import bp

def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('index.login'))
        return view(*args, **kwargs)
    return wrapped

@bp.route('/dashboard')
@login_required
def dashboard():
    # 从会话中获取用户名
    username = session.get('username')
    return render_template('dashboard.html', username=username)