from flask import Flask

from .exts import db, migrate
from .models import Files

def create_app(is_test=False):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECURE_KEY='dev',
    )

    if not is_test:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_pyfile('config_test.py', silent=True)
    
    # 初始化数据库
    db.init_app(app)
    migrate.init_app(app, db)

    # 注册路由
    from .route.upload import bp as upload_bp
    from .route.main import bp as index_bp

    app.register_blueprint(upload_bp)
    app.register_blueprint(index_bp)

    return app