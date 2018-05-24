# encoding: utf-8

"""
@author: leason
@time: 2017/11/14 11:01
"""
import threading
import traceback

from conf import web
from lib.exception.validator import JSONValidateError
from lib.flask import app
from lib.utils import build_ret, err_ret
from lib.utils import logging
from msg import msg

err_id = threading._get_ident()
FAIL = msg.ERROR
MSG = FAIL(1, "操作失败", err_id)


# 异常统一处理
@app.errorhandler(JSONValidateError)
def json_validate_error(e):
    MSG.msg = str(e)
    response = err_ret(MSG)
    logging.error("err_id:{}{}".format(err_id,traceback.format_exc()))
    return response


@app.errorhandler(Exception)
def internal_error(e):
    if web['debug']:
        response = err_ret(MSG)
    else:
        response = err_ret(MSG)
    logging.error("err_id:{}{}".format(err_id, traceback.format_exc()))
    return response


# 处理404页面
@app.errorhandler(404)
def not_found(e):
    response = build_ret(False, msg="页面不存在")
    return response


# 处理400页面
@app.errorhandler(400)
def bad_request(e):
    response = build_ret(False, msg="请求错误", code=err_id)
    logging.error("err_id:{}{}".format(err_id,traceback.format_exc()))
    return response

