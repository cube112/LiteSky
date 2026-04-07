from flask import render_template, send_file

from . import bp

@bp.route('/download')
def download():
    return send_file('path/to/your/file', as_attachment=True)