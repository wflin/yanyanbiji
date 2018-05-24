#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/11/17 15:45
"""
import os
from flask import request
from lib.flask import app
from lib.utils.common import get_uuid, date_time, build_ret
from app import route
from conf import web


ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif', 'PNG', 'JPG', 'JPEG', 'GIF']


app.config['UPLOAD_FOLDER'] = web['upload_path']

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
html = '''
    <!DOCTYPE html>
    <title>Upload File</title>
    <h1>图片上传</h1>
    <form method=post enctype=multipart/form-data>
         <input type=file name=file multiple=multiple>
         <input type=submit value=上传>
    </form>
    '''


@route("/upload", authentication=True, methods=['GET', 'POST'])
def uploads_images():
    if request.method == 'POST':

        date = date_time(fmt="%Y%m%d")

        files = request.files.getlist('file')

        file_urls = []
        for each_file in files:
            if each_file and allowed_file(each_file.filename):
                filename = get_uuid() + '.png'
                files_path = check_file_path(app.config['UPLOAD_FOLDER'], date)
                each_file.save(os.path.join(files_path, filename))
                file_url = web['pic_pix'] + "uploads/" + date + "/" + filename
                file_urls.append(file_url)
        result = {
            'file_url': file_urls
        }
        return build_ret(success=True, data=result)
    return html


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def check_file_path(file_path, date):
    if file_path[0] == ".":
        cwd = os.getcwd()
        re_file_path = os.path.abspath(file_path)
        file_dir = os.path.join(re_file_path, date)
        # 判断存储路径是否存在
        if os.path.isdir(file_dir):
            return file_dir
        else:
            os.chdir(file_path)
            os.mkdir(date)
            os.chdir(cwd)
            return file_dir
    else:
        file_dir = os.path.join(file_path, date)
        # 判断存储路径是否存在
        if os.path.isdir(file_dir):
            return file_dir
        else:
            os.chdir(file_path)
            os.mkdir(date)
            return file_dir