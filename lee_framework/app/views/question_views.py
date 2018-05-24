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
from app.services.question_service import add_question_service, modify_question_service, delete_question_service, \
    list_question_service, detail_question_service, add_reply_service, agree_reply_service, list_reply_service, \
    thumb_reply_service, report_reply_service


@route("/question/add", authentication=True, methods=['POST'])
def question_add():
    params = get_params()
    params["publisher_id"] = get_user_info()["user_id"]
    state = add_question_service(get_params())
    if state:
        return success_ret(msg.SUCCESS)
    else:
        return err_ret(msg.ERROR(1, "添加失败！"))


@route("/question/modify", authentication=True, methods=['POST'])
def question_modify():
    state = modify_question_service(get_params())
    if state:
        return success_ret(msg.SUCCESS)
    else:
        return err_ret(msg.ERROR(1, "修改失败！"))


@route("/question/delete", authentication=True, methods=['POST'])
def question_delete():
    state = delete_question_service(get_params()["id"])
    if state:
        return success_ret(msg.SUCCESS)
    else:
        return err_ret(msg.ERROR(1, "删除失败！"))


# 查询用户提出问题
@route("/question/list", authentication=True, methods=['POST'])
def question_list():
    params = get_params()
    params["user_id"] = get_user_info()["user_id"]
    state, result, total = list_question_service(params)
    if state:
        return build_ret(success=state, msg='操作成功', total=total, data=result)
    else:
        return err_ret(msg.ERROR(1, "查询失败！"))


# 查询所有问题
@route("/question/all", authentication=False, methods=['POST'])
def question_list():
    params = get_params()
    state, result, total = list_question_service(params)
    if state:
        return build_ret(success=state, msg='操作成功', total=total, data=result)
    else:
        return err_ret(msg.ERROR(1, "查询失败！"))


@route("/question/detail", authentication=False, methods=['POST'])
def question_detail():
    params = get_params()
    result = detail_question_service(params["id"])

    return build_ret(success=True, msg='操作成功', total=1, data=result)


# 回答问题
@route("/reply/add", authentication=True, methods=['POST'])
def reply_add():
    state = add_reply_service(get_params())
    if state:
        return success_ret(msg.SUCCESS)
    else:
        return err_ret(msg.ERROR(1, "添加失败！"))


# 查询问题评论
@route("/reply/list", authentication=False, methods=['POST'])
def reply_list():
    params = get_params()
    state, result, total = list_reply_service(params)
    if state:
        return build_ret(success=state, msg='操作成功', total=total, data=result)
    else:
        return err_ret(msg.ERROR(1, "查询失败！"))


@route("/reply/thumb", authentication=True, methods=['POST'])
def reply_thumb():
    params = get_params()
    state, result = thumb_reply_service(params)

    if state:
        return success_ret(msg.SUCCESS)
    else:
        return err_ret(result)


@route("/reply/agree", authentication=True, methods=['POST'])
def reply_agree():
    params = get_params()
    state, result = agree_reply_service(params)

    if state:
        return success_ret(msg.SUCCESS)
    else:
        return err_ret(result)


# 管理员查询所有问题
@route("/admin/question/list", authentication=True, methods=['POST'])
def admin_question_list():
    params = get_params()
    state, result, total = list_question_service(params)
    if state:
        return build_ret(success=state, msg='操作成功', total=total, data=result)
    else:
        return err_ret(msg.ERROR(1, "查询失败！"))


# 管理员编辑问题
@route("/admin/question/modify", authentication=True, methods=['POST'])
def admin_question_modify():
    """
    id:1,
    status:2, 2违规
    :return:
    """
    state = modify_question_service(get_params())
    if state:
        return success_ret(msg.SUCCESS)
    else:
        return err_ret(msg.ERROR(1, "修改失败！"))


# 管理员查询问题评论
@route("/admin/reply/list", authentication=True, methods=['POST'])
def admin_reply_list():
    params = get_params()
    state, result, total = list_reply_service(params)
    if state:
        return build_ret(success=state, msg='操作成功', total=total, data=result)
    else:
        return err_ret(msg.ERROR(1, "查询失败！"))


# 管理员修改评论状态
@route("/admin/reply/modify", authentication=True, methods=['POST'])
def admin_reply_modify():
    state = report_reply_service(get_params())
    if state:
        return success_ret(msg.SUCCESS)
    else:
        return err_ret(msg.ERROR(1, "修改失败！"))