#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/11/14 16:25
"""
from flask import request, make_response
from lib.flask import app
from db import redis_conn as redis_server
from msg import msg
from conf import redis_pre, ex_time
from lib.utils.common import err_ret


# 访问速度控制
@app.before_request
def before_request():
    pass
    # get ip
    # ip = request.headers.get('X-Real-IP')
    # if ip is None or ip == '':
    #     ip = "127.0.0.1"
    # result = redis_server.get(redis_pre['access_pix'] + ip)
    # if result:
    #     return make_response(err_ret(msg.A_MAX_REQUEST))
    # else:
    #     redis_server.set(redis_pre['access_pix'] + ip, value=redis_pre['access_pix'] + ip, ex=ex_time['access_ex'])

