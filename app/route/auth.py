from datetime import date

from flask import Blueprint, request, session, g, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from ..exts import db
from ..models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')


# 在每次请求之前加载已登录的用户
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = db.session.scalar(db.select(User).where(User.id == user_id))


# ========
# 注册接口
# ========
@bp.route('/register', methods=['POST'])
def register():
    # 用户名
    username = request.form.get('username')
    # 邮箱
    email_name = request.form.get('email')
    email_domain = request.form.get('email_domain')
    email = f"{email_name}@{email_domain}"
    # 密码
    password = request.form.get('password')
    password_hash = generate_password_hash(password)
    # 注册日期
    register_date = date.today()
    # 错误信息
    error = None

    # 检查用户名、邮箱和密码是否提供
    if not username:
        error = '用户名不能为空'
    elif not email_name or not email_domain:
        error = '邮箱不能为空'
    elif not password:
        error = '密码不能为空'

    # 检查用户名和邮箱是否已存在
    if error is None:
        try:
            new_user = User(username=username, email=email, password=password_hash, created_at=register_date)
            db.session.add(new_user)
            db.session.commit()
        except db.IntegrityError:
            error = '用户名或邮箱已存在'
        else:
            return "注册成功", 200


# ========
# 登录接口
# ========
@bp.route('/login', methods=['POST'])
def login():
    # 从from表单获取邮箱和密码
    email_name = request.form.get('email')
    email_domain = request.form.get('email_domain')
    email = f"{email_name}@{email_domain}"
    password = request.form.get('password')

    user = db.session.scalar(db.select(User).where(User.email == email))
    if user and check_password_hash(user.password, password):
        session['user_id'] = user.id
        return "登录成功", 200
    return "登录失败", 400


# ========
# 登出接口
# ========
@bp.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for('index.index'))