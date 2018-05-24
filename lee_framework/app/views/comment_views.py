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
from app.services.comment_service import add_comment_service, list_comment_service, delete_comment_service


@route("/comment/add", authentication=True, methods=['POST'])
def commit_add():
    params = get_params()
    params["user_id"] = get_user_info()["user_id"]
    state = add_comment_service(get_params())
    if state:
        return success_ret(msg.SUCCESS)
    else:
        return err_ret(msg.ERROR(1, "添加失败！"))


@route("/comment/delete", authentication=True, methods=['POST'])
def commit_delete():
    state = delete_comment_service(get_params()["id"], get_user_info()["user_id"])
    if state:
        return success_ret(msg.SUCCESS)
    else:
        return err_ret(msg.ERROR(1, "删除失败！"))


@route("/comment/list", authentication=True, methods=['POST'])
def commit_list():
    params = get_params()
    params["user_id"] = get_user_info()["user_id"]
    state, result, total = list_comment_service(params)
    if state:
        return build_ret(success=state, msg='操作成功', total=total, data=result)
    else:
        return err_ret(msg.ERROR(1, "查询失败！"))