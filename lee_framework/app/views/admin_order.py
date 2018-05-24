#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/11/14 11:01
"""
from app import route
from app.services.admin_order import list_order_admin, status_order_admin
from app.utils.get_info import get_params, get_user_info
from msg import msg
from lib.utils.common import build_ret, err_ret, success_ret


@route("/admin/order/list", authentication=True, methods=['POST'])
def admin_order_list():
    params = get_params()
    state, result, total = list_order_admin(params)
    if state:
        return build_ret(success=state, msg='操作成功', total=total, data=result)
    else:
        return err_ret(msg.ERROR(1, "查询失败！"))


@route("/admin/order/status", authentication=True, methods=['POST'])
def admin_order_modify():
    state = status_order_admin(get_params())
    if state:
        return success_ret(msg.SUCCESS)
    else:
        return err_ret(msg.ERROR(1, "修改失败！"))