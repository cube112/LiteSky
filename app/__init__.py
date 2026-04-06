from flask import Flask
from flask import session, g

from .exts import db, migrate
from .models import User
from .models import Files


def create_app(is_test=True):
    app = Flask(__name__, instance_relative_config=True)

    if not is_test:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_pyfile('config_test.py', silent=True)
    
    # 在收到任意一个请求后，将用户信息存储在全局对象 g 中
    @app.before_request
    def load_user():
        user_id = session.get('user_id')
        if user_id is None:
            g.user = None
        else:
            g.user = db.session.scalar(db.select(User).where(User.id == user_id))

    # 初始化数据库
    db.init_app(app)
    migrate.init_app(app, db)

    # 注册路由
    from .route.upload import bp as upload_bp
    from .route.main import bp as index_bp
    from .route.auth import bp as auth_bp

    app.register_blueprint(upload_bp)
    app.register_blueprint(index_bp)
    app.register_blueprint(auth_bp)

    return app