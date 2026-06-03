import os
import uuid
from datetime import datetime, timedelta

from flask import Blueprint, request, current_app, g

from ..exts import db
from ..models import Files


bp = Blueprint('file', __name__, url_prefix='/file')


@bp.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    if file:
        origin_filename = file.filename
        store_filename = uuid.uuid4().hex
        save_path = os.path.join('uploads', store_filename)

        file.seek(0, os.SEEK_END)
        file_size = file.tell()
        file.seek(0)

        upload_time = datetime.now()
        delete_time = datetime.now() + timedelta(days=current_app.config['FILE_DELETE_DAYS'])

        download_code = uuid.uuid4().hex[: 8: 2]
        if db.session.scalar(db.select(Files).where(Files.download_code == download_code)):
            download_code = uuid.uuid4().hex[: 8: 2]

        user_id = g.user.id

        new_file = Files(
            origin_filename=origin_filename,
            store_filename=store_filename,
            save_path=save_path,
            file_size=file_size,
            upload_time=upload_time,
            delete_time=delete_time,
            download_code=download_code,
            user_id=user_id
        )
        try:
            db.session.add(new_file)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return f"文件上传失败: {str(e)}", 500
        
        try:
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], store_filename))
        except Exception as e:
            db.session.delete(new_file)
            db.session.commit()
            return f"文件保存失败: {str(e)}", 500
        
        return "文件上传成功", 200