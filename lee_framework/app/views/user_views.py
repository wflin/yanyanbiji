#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/11/14 11:01
"""
from flask import make_response, request
from app import route
from app.services.user_service import admin_login_service, admin_user_balance, admin_user_list, user_info
from app.utils.get_info import get_params, get_user_info
from msg import msg
from lib.utils.common import build_ret, err_ret, success_ret

from app.pretreatment.user_pretreat import login_pretreat, logout_pretreat, user_register, ver_code, user_modify, password_modify, password_forget, payword_forget


@route("/user/login", authentication=False, methods=['POST'])
def login():
    state, token = login_pretreat()
    if state:
        resp = success_ret(msg.LOGIN_SUCCESS)
        response = make_response(resp)
        response.headers['authorization'] = token
        return response
    else:
        return err_ret(msg.A_LOGIN_ERR)


@route("/user/logout", authentication=True, methods=['GET'])
def logout():
    token = request.headers.get('authorization')
    state = logout_pretreat(token)
    if state:
        return success_ret(msg.LOGOUT_SUCCESS)
    else:
        return err_ret(msg.A_TIMEOUT)


@route("/user/register", authentication=False, methods=['POST'])
def register():
    state, result = user_register()
    if state:
        resp = success_ret(msg.SUCCESS)
        response = make_response(resp)
        response.headers['authorization'] = result
        return response
    else:
        return err_ret(result)


@route("/user/code", authentication=False, methods=['GET'])
def code():
    state = ver_code()
    if state:
        return success_ret(msg.SUCCESS)
    else:
        return err_ret(msg.A_MAX_REQUEST)


@route("/user/modify", authentication=True, methods=['POST'])
def modify():
    state, result = user_modify()
    if state:
        return success_ret(msg.SUCCESS)
    else:
        return err_ret(msg.ERROR(1, "操作失败！"))


@route("/password/forget", authentication=False, methods=['POST'])
def forget_password():
    state, result = password_forget()
    if state:
        return success_ret(msg.SUCCESS)
    else:
        return err_ret(result)


@route("/password/modify", authentication=True, methods=['POST'])
def modify_password():
    state, result = password_modify()
    if state:
        return success_ret(msg.SUCCESS)
    else:
        return err_ret(result)


@route("/payword/forget", authentication=True, methods=['POST'])
def forget_payword():
    state, result = payword_forget()
    if state:
        return success_ret(msg.SUCCESS)
    else:
        return err_ret(result)


@route("/payword/set", authentication=True, methods=['POST'])
def set_payword():
    state, result = payword_forget()
    if state:
        return success_ret(msg.SUCCESS)
    else:
        return err_ret(result)


# 用户查询
@route("/user/info", authentication=True, methods=['POST'])
def admin_user_list_():
    user_id = get_user_info()["user_id"]
    result = user_info(user_id)
    return build_ret(success=True, msg='操作成功', data=result)


# 管理员登录
@route("/admin/login", authentication=False, methods=['POST'])
def admin_login():
    params = get_params()
    state, token = admin_login_service(params["username"], params["password"])
    if state:
        resp = success_ret(msg.LOGIN_SUCCESS)
        response = make_response(resp)
        response.headers['authorization'] = token
        return response
    else:
        return err_ret(msg.A_LOGIN_ERR)


# 用户查询
@route("/admin/user/list", authentication=True, methods=['POST'])
def admin_user_list_():
    params = get_params()
    result, total = admin_user_list(params)
    return build_ret(success=True, msg='操作成功', total=total, data=result)


# 用户充值
@route("/admin/user/charge", authentication=True, methods=['POST'])
def admin_user_charge():
    params = get_params()
    admin_user_balance(params["telephone"], params["money"])
    return build_ret(success=True, msg='操作成功')