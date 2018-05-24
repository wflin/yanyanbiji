#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/11/15 15:07
"""
from flask import g
from sqlalchemy import and_

from app.models.user_models import User, Admin
from app.utils.get_info import get_session
from app.utils.opreate_token import en_token
from conf import redis_pre
from msg import msg
from db import redis_conn as redis_server


@get_session
def login_service(telephone):
    """
    登录
    :param telephone:
    :return:
    """
    session = g.session
    user_id, telephone, password = session.query(User.id, User.telephone, User.password).filter(User.telephone == telephone).one_or_none()
    result = dict()
    if telephone is not None:
        result['telephone'] = telephone
        result['password'] = password
        result['id'] = user_id
        return True, result

    return False, result


@get_session
def register(telephone, password):
    """
    手机验证码注册
    :param telephone:
    :param password:
    :return:
    """
    session = g.session
    result = session.query(User).filter(User.username == telephone).one_or_none()
    if result:
        return False, msg.A_EXIST
    model = User(telephone=telephone, password=password)
    session.add(model)
    session.flush()
    model_id = model.id
    session.commit()
    return True, model_id


@get_session
def modify_service(telephone, params):
    """
    用户信息编辑
    :param params:{
        # "telephone":"1321646841",
        "username":"xxxxx",
        "school":"school",
        "address":"address",
        "pic":"pic"
    }
    :return:
    """
    session = g.session
    result = session.query(User).filter(User.telephone == telephone).one_or_none()
    if result:
        result.username = params["username"]
        result.school = params["school"]
        result.address = params["address"]
        result.pic = params.get("pic")
        session.commit()
        return True, msg.SUCCESS
    return False, msg.ERROR(1, "用户不存在！")


@get_session
def forget_password_service(telephone, password):
    """
    忘记密码
    :param password:密码
    :return:
    """
    session = g.session
    result = session.query(User).filter(User.telephone == telephone).one_or_none()
    if result:
        result.password = password
        session.commit()
        return True, msg.SUCCESS
    return False, msg.ERROR(1, "用户不存在！")


@get_session
def modify_password_service(telephone, password, old_password):
    """
    修改密码
    :param password:密码
    :return:
    """
    session = g.session
    result = session.query(User).filter(User.telephone == telephone).filter(User.password == old_password).one_or_none()
    if result:
        result.password = password
        session.commit()
        return True, msg.SUCCESS
    return False, msg.ERROR(1, "密码有误！")


@get_session
def forget_payword_service(telephone, pay_password):
    """
    忘记密码
    :param password:密码
    :return:
    """
    session = g.session
    result = session.query(User).filter(User.telephone == telephone).one_or_none()
    if result:
        result.pay_password = pay_password
        session.commit()
        return True, msg.SUCCESS
    return False, msg.ERROR(1, "用户不存在！")


@get_session
def user_info(user_id):
    """
    用户信息查询
    :param user_id: 用户id
    :return:
    """
    session = g.session
    result = session.query(User).filter(User.id == user_id).one()
    return result.to_json()


@get_session
def admin_login_service(username, password):
    """
    管理员登录
    :param username: 用户名
    :param password: 密码
    :return:
    """
    session = g.session
    result = session.query(Admin).filter(and_(
        Admin.username == username,
        Admin.password == password
    )).one_or_none()
    if result:
        token = en_token(user_id=result.id, telephone=username)
        redis_server.set(redis_pre['token_pix'] + username, token)
        return True, token
    return False, None


@get_session
def admin_user_list(data):
    """
    用户查询
    :param data:{
        "limit":10,
        "page":10,
        "cond":{
            "telephone":"15879179253",
            "start_time": "2017-10-01",
            "end_time": "2017-10-09"
        }
    }
    :return:
    """
    session = g.session
    # 分页
    limit = data['limit']
    offset = (data['page'] - 1) * data['limit']
    cond = data["cond"]
    sql_result = session.query(User).filter(and_(
        User.telephone.like('%' + str(cond['telephone']) + '%'),
        User.create_time.between(cond['start_time'], cond['end_time'])
    ))
    total = sql_result.count()
    sql_content = sql_result.order_by(User.create_time.desc()).limit(limit).offset(offset)
    result = [i.admin_to_json() for i in sql_content]

    return result, total


@get_session
def admin_user_balance(telephone, money):
    """
    用户充值
    :param telephone:
    :param money:
    :return:
    """
    session = g.session
    result = session.query(User).filter(User.telephone==telephone).one()
    result.balance = result.balance + int(money)
    session.commit()
    return True