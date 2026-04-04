from flask import render_template

from . import bp

@bp.route('/')
def doc():
    return render_template('doc.html')