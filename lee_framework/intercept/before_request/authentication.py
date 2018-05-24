#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/11/14 15:22
"""

from flask import g, request, make_response
from lib.flask import app
from lib.decorators.before_route import login_list
from db import redis_conn as redis_server
from msg import msg
from conf import redis_pre
from lib.utils.common import err_ret
from app.utils.opreate_token import de_token


# 身份认证
@app.before_request
def authorization():
    path = request.path
    if path not in login_list and str(request.method) not in ['OPTIONS']:
        token = request.headers.get('authorization')
        re_bool, info = token_check(request_token=token)
        g.user_info = info
        if not re_bool:
            return info
        account = info['telephone']
        re_bool, resp = login_status_check(account=account, request_token=token)
        if not re_bool:
            return resp


def login_status_check(account, request_token):
    redis_token = redis_server.get(redis_pre['token_pix'] + account)
    if not (redis_token == request_token):
        return False, make_response(err_ret(msg.A_SIGNED))
    return True, True


def token_check(request_token):
    account_info = de_token(request_token)
    if not account_info:
        return False, make_response(err_ret(msg.A_TIMEOUT))
    return True, account_info
