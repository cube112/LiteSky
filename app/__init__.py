from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_login import LoginManager

from .blueprint import register_blueprints
from .models import Files, Users


def create_app(test_config: dict | None = None) -> Flask:
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    # 初始化数据库
    from .exts import db, migrate

    db.init_app(app)
    migrate.init_app(app, db)

    # 初始化限流器
    limiter = Limiter(key_func=get_remote_address, default_limits=["5 per minute"])
    limiter.init_app(app)

    # 初始化登录管理器
    login_manager = LoginManager()
    login_manager.init_app(app)

    # 注册蓝图
    register_blueprints(app)

    return app
