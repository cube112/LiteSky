from flask import render_template, url_for, request, redirect, session, g


from ...exts import db
from ...models import User
from . import bp

@bp.route('/')
def index():
    return render_template('index.html')
