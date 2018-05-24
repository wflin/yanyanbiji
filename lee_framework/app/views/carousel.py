#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/11/14 11:01
"""
from app import route
from app.services.carousel import list_carousel, add_carousel, delete_carousel
from app.services.report import add_report, list_report
from app.utils.get_info import get_params
from lib.utils.common import build_ret, err_ret, success_ret
from msg import msg


@route("/admin/carousel/list", authentication=False, methods=['POST'])
def admin_carousel_list():
    params = get_params()
    state, result, total = list_carousel(params)
    if state:
        return build_ret(success=state, msg='操作成功', total=total, data=result)
    else:
        return err_ret(msg.ERROR(1, "查询失败！"))


@route("/admin/carousel/add", authentication=True, methods=['POST'])
def admin_carousel_add():
    add_carousel(get_params())
    return success_ret(msg.SUCCESS)


@route("/admin/carousel/delete", authentication=True, methods=['POST'])
def admin_carousel_delete():
    delete_carousel(get_params()["id"])
    return success_ret(msg.SUCCESS)


@route("/carousel/list", authentication=False, methods=['POST'])
def admin_carousel_list():
    params = get_params()
    state, result, total = list_carousel(params)
    if state:
        return build_ret(success=state, msg='操作成功', total=total, data=result)
    else:
        return err_ret(msg.ERROR(1, "查询失败！"))


# 举报
@route("/admin/report/list", authentication=False, methods=['POST'])
def admin_report_list():
    params = get_params()
    state, result, total = list_report(params)
    if state:
        return build_ret(success=state, msg='操作成功', total=total, data=result)
    else:
        return err_ret(msg.ERROR(1, "查询失败！"))


@route("/report/add", authentication=True, methods=['POST'])
def report_add():
    add_report(get_params())
    return success_ret(msg.SUCCESS)