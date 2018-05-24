#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/11/14 9:54
"""
from flask import g
from lib.flask import app
from lib.utils import logging


@app.after_request
def response_handler(response):
    # 关闭session
    try:
        g.session.close()
    except:
        pass
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type,authorization,Captcha-ETag'
    response.headers['Access-Control-Expose-Headers'] = 'authorization, Captcha-ETag'
    if not(response.headers['Content-Type'] == "image/png"):
        logging.info("response is [{}]".format(response.data))
    return response

