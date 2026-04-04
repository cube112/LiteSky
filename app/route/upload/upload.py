from flask import request, render_template
from flask import current_app
from flask import jsonify

from ...models import Files
from ...exts import db

import uuid
import os
from datetime import datetime, timedelta

from . import bp

def allowed_file(filename):
    ALLOWED_EXTENSIONS = current_app.config['ALLOWED_EXTENSIONS']
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# 定义一个函数，输入是文件字节数，输出是一个字符串，表示文件大小，单位是B、KB、MB、GB等
def format_file_size(file_size):
    if file_size < 1024:
        return f"{file_size} B"
    elif file_size < 1024 * 1024:
        return f"{file_size / 1024:.2f} KB"
    elif file_size < 1024 * 1024 * 1024:
        return f"{file_size / (1024 * 1024):.2f} MB"
    else:
        return f"{file_size / (1024 * 1024 * 1024):.2f} GB"

@bp.route('/', methods=['GET', 'POST'])
# 如果是GET请求，返回上传页面；如果是POST请求，处理上传的文件
def upload():
    if request.method == 'POST':
        # 获取上传的文件
        if 'file' not in request.files:
            return jsonify({
                'error': '? 老大，你无敌了。'
                }), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({
                'error': '老大，不上传文件来干什么喵？'
                }), 400
        
        if file and allowed_file(file.filename):
            # 原始文件名
            origin_filename = file.filename

            # 存储文件名，使用UUID避免冲突
            ext = origin_filename.rsplit('.', 1)[1].lower()
            store_filename = f"{uuid.uuid4().hex}.{ext}"

            # 文件保存路径
            current_day = datetime.now().strftime('%Y-%m-%d')
            save_path = os.path.join(current_app.config['UPLOAD_FOLDER'], current_day)
            
            # 文件大小
            file_size = format_file_size(file.content_length)

            # 文件上传时间和删除时间
            upload_time = datetime.now()
            delete_time = (upload_time + timedelta(days=current_app.config['FILE_DELETE_DAYS']))

            # 准备写入数据库
            upload_file = Files(
                origin_filename=origin_filename,
                store_filename=store_filename,
                save_path=save_path,
                file_size=file_size,
                upload_time=upload_time,
                delete_time=delete_time
            )

            # 保存文件到磁盘，如果保存路径不存在则创建
            try:
                os.makedirs(save_path, exist_ok=True)
                file.save(os.path.join(save_path, store_filename))
                
                db.session.add(upload_file)
                db.session.commit()
                return jsonify({
                    'message': '文件上传成功',
                    'origin_filename': origin_filename,
                    'file_size': file_size,
                    'upload_time': upload_time.strftime('%Y-%m-%d %H:%M:%S'),
                    'delete_time': delete_time.strftime('%Y-%m-%d %H:%M:%S')
                }), 201
            except Exception as e:
                return jsonify({
                    'error': f'老大，文件保存失败了喵: {str(e)}'
                }), 500
            
        else:
            return jsonify({
                'error': '不是哥们'
            }), 400

    elif request.method == 'GET':
        return render_template('upload.html')
    
    else:
        return jsonify({
            'error': '老大，你在搞什么飞机喵？'
        }), 405