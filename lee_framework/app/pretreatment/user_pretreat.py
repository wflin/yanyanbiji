#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/11/15 14:13
"""
from app.utils.get_info import get_params, get_user_info
from app.utils.opreate_token import en_token
from app.utils.public_moethods import generate_code
from app.utils.sms_aliyun import send
from conf import redis_pre
from db import redis_conn as redis_server
from msg import msg

from app.services.user_service import login_service, register, modify_service, modify_password_service, forget_password_service, forget_payword_service
import json


def login_pretreat():
    """
    登录处理
    :return:state, token
    """
    params = get_params()
    state, result = login_service(params['telephone'])
    if state:
        if result["password"] == params['password']:
            token = en_token(user_id=result["id"], telephone=params['telephone'])
            redis_server.set(redis_pre['token_pix'] + params['telephone'], token)
            return True, token

    return False, None


def logout_pretreat(token):
    """
    登出
    :param token:
    :return:
    """
    redis_server.delete(token)
    telephone = get_user_info()['telephone']
    redis_server.delete(redis_pre['token_pix'] + telephone)

    return True


def user_register():
    """
    注册
    :return:
    """
    params = get_params()
    telephone = params["telephone"]
    # redis验证码和前端验证码比较
    code = redis_server.get(redis_pre['register_sms'] + str(telephone))
    if code and int(params["code"]) == int(code):
        redis_server.delete(redis_pre['register_sms'] + str(telephone))
        state, result = register(params["telephone"], params["password"])
        if state:
            token = en_token(user_id=result, telephone=params['telephone'])
            redis_server.set(redis_pre['token_pix'] + params['telephone'], token)
            return True, token
        return state, result
    return False, msg.A_CODE_TIMEOUT


def ver_code():
    """
    验证码
    :return:
    """
    params = get_params()
    telephone = params["telephone"]
    code = dict()
    code["code"] = generate_code()
    redis_server.set(redis_pre['register_sms'] + str(telephone), code["code"], 60)
    # 阿里大鱼发送验证码
    result = json.loads(send(code["code"], str(telephone)))
    print result
    if result["Code"] == "OK":
        return True
    return False


def user_modify():
    """
    用户编辑
    :return:
    """
    params = get_params()
    telephone = get_user_info()["telephone"]
    return modify_service(telephone, params)


def password_forget():
    """
    忘记密码 密码修改
    :return:
    """
    params = get_params()
    telephone = get_params()["telephone"]
    # redis验证码和前端验证码比较
    code = redis_server.get(redis_pre['register_sms'] + str(telephone))
    if code and int(params["code"]) == int(code):
        redis_server.delete(redis_pre['register_sms'] + str(telephone))
        return forget_password_service(telephone, params["password"])
    return False, msg.A_CODE_TIMEOUT


def password_modify():
    """
    密码修改
    :return:
    """
    params = get_params()
    telephone = get_user_info()["telephone"]
    return modify_password_service(telephone, params["password"], params["old_password"])


def payword_forget():
    """
    忘记支付密码
    :return:
    """
    params = get_params()
    telephone = get_user_info()["telephone"]
    # redis验证码和前端验证码比较
    code = redis_server.get(redis_pre['register_sms'] + str(telephone))
    if code and int(params["code"]) == int(code):
        redis_server.delete(redis_pre['register_sms'] + str(telephone))
        return forget_payword_service(telephone, params["pay_password"])
    return False, msg.A_CODE_TIMEOUT