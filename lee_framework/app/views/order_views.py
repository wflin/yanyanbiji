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
from app.services.order_service import add_order_service, list_order_service, detail_order_service, deliver_order_service, status_order_service


@route("/order/add", authentication=True, methods=['POST'])
def order_add():
    state = add_order_service(get_params()["items"])
    if state:
        return success_ret(msg.SUCCESS)
    else:
        return err_ret(msg.ERROR(1, "添加失败！"))


@route("/order/detail", authentication=True, methods=['POST'])
def product_delete():
    params = get_params()
    result = detail_order_service(params["id"])

    return build_ret(success=True, msg='操作成功', total=1, data=result)


@route("/order/list", authentication=True, methods=['POST'])
def order_list():
    params = get_params()
    state, result, total = list_order_service(params)
    if state:
        return build_ret(success=state, msg='操作成功', total=total, data=result)
    else:
        return err_ret(msg.ERROR(1, "查询失败！"))


@route("/order/deliver", authentication=True, methods=['POST'])
def order_deliver():
    state = deliver_order_service(get_params())
    if state:
        return success_ret(msg.SUCCESS)
    else:
        return err_ret(msg.ERROR(1, "修改失败！"))


@route("/order/status", authentication=True, methods=['POST'])
def order_modify():
    state = status_order_service(get_params())
    if state:
        return success_ret(msg.SUCCESS)
    else:
        return err_ret(msg.ERROR(1, "修改失败！"))