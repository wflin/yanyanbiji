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
from app.services.product_service import add_product_service, modify_product_service, delete_product_service, \
    list_product_service, all_product_service, detail_product_service


@route("/product/add", authentication=True, methods=['POST'])
def product_add():
    params = get_params()
    params["publisher_id"] = get_user_info()["user_id"]
    state = add_product_service(get_params())
    if state:
        return success_ret(msg.SUCCESS)
    else:
        return err_ret(msg.ERROR(1, "添加失败！"))


@route("/product/modify", authentication=True, methods=['POST'])
def product_modify():
    state = modify_product_service(get_params())
    if state:
        return success_ret(msg.SUCCESS)
    else:
        return err_ret(msg.ERROR(1, "修改失败！"))


@route("/product/delete", authentication=True, methods=['POST'])
def product_delete():
    state = delete_product_service(get_params()["id"])
    if state:
        return success_ret(msg.SUCCESS)
    else:
        return err_ret(msg.ERROR(1, "删除失败！"))


@route("/product/list", authentication=True, methods=['POST'])
def product_list():
    params = get_params()
    params["user_id"] = get_user_info()["user_id"]
    state, result, total = list_product_service(params)
    if state:
        return build_ret(success=state, msg='操作成功', total=total, data=result)
    else:
        return err_ret(msg.ERROR(1, "查询失败！"))


@route("/product/all", authentication=False, methods=['POST'])
def product_all():
    params = get_params()
    state, result, total = all_product_service(params)
    if state:
        return build_ret(success=state, msg='操作成功', total=total, data=result)
    else:
        return err_ret(msg.ERROR(1, "查询失败！"))


@route("/product/detail", authentication=False, methods=['POST'])
def product_detail():
    params = get_params()
    result = detail_product_service(params["id"])

    return build_ret(success=True, msg='操作成功', total=1, data=result)


# 管理员 查询产品
@route("/admin/product/list", authentication=False, methods=['POST'])
def admin_product_list():
    params = get_params()
    state, result, total = all_product_service(params)
    if state:
        return build_ret(success=state, msg='操作成功', total=total, data=result)
    else:
        return err_ret(msg.ERROR(1, "查询失败！"))


@route("/admin/product/modify", authentication=True, methods=['POST'])
def admin_product_modify():
    """
    "id":465464,
    "status": 2,
    :return:
    """
    state = modify_product_service(get_params())
    if state:
        return success_ret(msg.SUCCESS)
    else:
        return err_ret(msg.ERROR(1, "修改失败！"))