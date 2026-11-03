# 2026/11/03 Written by _Zeroverse
# Blueprint module for the application

# register all blueprints
from .src.service.identify import identify_bp


def register_blueprints(app):
    app.register_blueprint(identify_bp)
