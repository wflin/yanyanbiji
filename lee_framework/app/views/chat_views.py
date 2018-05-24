#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/12/14 11:01
"""
from app import route
from app.utils.get_info import get_params, get_user_info
from msg import msg
from lib.utils.common import build_ret, err_ret, success_ret
from app.services.chat_service import add_chat_service, list_chat_service, status_chat_service


@route("/chat/add", authentication=True, methods=['POST'])
def chat_add():
    state = add_chat_service(get_params())
    if state is True:
        return success_ret(msg.SUCCESS)
    elif state == 2:
        return err_ret(msg.ERROR(1, "不能发给自己！"))
    else:
        return err_ret(msg.ERROR(1, "发送失败！"))


@route("/chat/list", authentication=True, methods=['POST'])
def chat_list():
    params = get_params()
    params["user_id"] = get_user_info()["user_id"]
    state, result, total = list_chat_service(params)
    if state:
        return build_ret(success=state, msg='操作成功', total=total, data=result)
    else:
        return err_ret(msg.ERROR(1, "查询失败！"))


@route("/chat/status", authentication=True, methods=['POST'])
def chat_status():
    params = get_params()
    params["user_id"] = get_user_info()["user_id"]
    state, result, total = status_chat_service(params)
    if state:
        return build_ret(success=state, msg='操作成功', total=total, data=result)
    else:
        return err_ret(msg.ERROR(1, "查询失败！"))