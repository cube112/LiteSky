import os

from flask import render_template, send_file, request, jsonify

from ...exts import db
from ...models import Files
from . import bp

@bp.route('/download')
def download():
    download_code = (request.args.get('download_code') or '').strip()
    file = db.session.scalar(db.select(Files).where(Files.download_code == download_code))
    if not file:
        return jsonify({'error': '下载码无效'}), 404
    
    filepath = os.path.join(file.save_path, file.store_filename)
    return send_file(filepath, as_attachment=True, download_name=file.origin_filename)
    
