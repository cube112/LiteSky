from flask import Flask

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

    register_blueprints(app)
    return app
