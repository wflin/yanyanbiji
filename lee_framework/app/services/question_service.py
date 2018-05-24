#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/01/04 15:07
"""
from flask import g
from sqlalchemy import and_

from app.models.product import Question, Reply
from app.models.user_models import User
from app.utils.get_info import get_session, get_user_info
from msg import msg


@get_session
def add_question_service(data):
    """
    提问
    :param data:{
        "name": "",
        "detail": "",
        # "publisher_id": self.publisher_id,
        "category": "",
        "price": 15212
    }
    :return:
    """
    session = g.session
    data["publisher_id"] = get_user_info()["user_id"]
    # 扣钱
    user_sql = session.query(User).filter(User.id == data["publisher_id"]).one()
    if user_sql.balance < int(data["price"]):
        return False
    user_sql.balance = user_sql.balance - int(data["price"])
    question = Question()
    for key, value in data.items():
        setattr(question, key, value)
    session.add(question)
    session.commit()
    return True


@get_session
def modify_question_service(data):
    """
    编辑问题
    :param data:{
        "id":465464,
        "name": "",
        "detail": "",
        "category": "",
        "price": 15212
    }
    :return:
    """
    session = g.session
    question_sql = session.query(Question).filter(Question.id == data.pop("id")).one_or_none()
    if question_sql:
        for key, value in data.items():
            setattr(question_sql, key, value)

        session.commit()

        return True
    return False


@get_session
def delete_question_service(question_id):
    """
    删除问题
    :param question_id:
    :return:
    """
    session = g.session
    product = session.query(Question).filter(Question.id == question_id).one_or_none()
    if product:
        session.delete(product)
        session.commit()
        return True
    return False


@get_session
def list_question_service(data):
    """
    用户查询发布的问题 或 查询所有问题
    :param data: {
        "cond":{
            "id": 1,
            "key_word": "sd",
            "status": 0, 0 未完成采纳 1 已采纳 2违规
            "category":0
        },
        "limit": 8,
        "page": 3

    }
    :return:
    """
    session = g.session
    # 分页
    limit = data['limit']
    offset = (data['page'] - 1) * data['limit']
    cond = data["cond"]
    if cond["status"] or int(cond["status"])==0:
        cond["status"] = [cond["status"]]
    else:
        cond["status"] = [1, 2]

    sql_result = session.query(Question).filter(and_(
        Question.id == cond["id"] if cond.get('id') is not None else "",
        Question.publisher_id == data["user_id"] if data.get('user_id') is not None else "",
        Question.status.in_(cond['status']),
        Question.name.like('%' + str(cond['key_word']) + '%') if cond['key_word'] is not None else "",
        Question.category.like('%' + str(cond['category']) + '%') if cond['category'] is not None else ""
    ))
    total = sql_result.count()
    sql_content = sql_result.order_by(Question.create_time.desc()).limit(limit).offset(offset)
    result = [i.to_json() for i in sql_content]

    return True, result, total


@get_session
def detail_question_service(question_id):
    """
    问题详情
    :param question_id:
    :return:
    """
    session = g.session
    product = session.query(Question).filter(Question.id == question_id).one()
    return product.to_json()


@get_session
def add_reply_service(data):
    """
    回答提问
    :param data:{
        "content": self.content,
        "question_id": self.question_id
    }
    :return:
    """
    session = g.session
    data["reply_id"] = get_user_info()["user_id"]
    reply = Reply()
    for key, value in data.items():
        setattr(reply, key, value)
    session.add(reply)
    session.commit()
    return True


@get_session
def list_reply_service(data):
    """
    查询问题评论
    :param data: {
        "id":123,
        "question_id":451
        "limit": 8,
        "page": 1
    }
    :return:
    """
    session = g.session
    # 分页
    limit = data['limit']
    offset = (data['page'] - 1) * data['limit']

    sql_result = session.query(Reply).filter(and_(
        Reply.question_id == data["question_id"] if data.get("question_id") else "",
        Reply.question_id == data["id"] if data.get("id") else ""
    ))
    total = sql_result.count()
    sql_content = sql_result.order_by(Reply.create_time.desc()).limit(limit).offset(offset)
    result = [i.to_json() for i in sql_content]

    return True, result, total


@get_session
def thumb_reply_service(data):
    """
    点赞
    :param data:{
        "id":465464
    }
    :return:
    """
    session = g.session
    user_id = get_user_info()["user_id"]
    question_sql = session.query(Reply).filter(Reply.id == data.pop("id")).one()
    question_sql.thumbs_num += 1
    if user_id in question_sql.thumbs_user.split(","):
        return False, msg.ERROR(1, "已点赞！")
    question_sql.thumbs_user = question_sql.thumbs_user + "," + str(user_id)
    session.commit()

    return True, msg.SUCCESS


@get_session
def agree_reply_service(data):
    """
    采纳回复
    :param data:{
        "id":465464
    }
    :return:
    """
    session = g.session
    user_id = get_user_info()["user_id"]
    reply_sql = session.query(Reply).filter(Reply.id == data.pop("id")).one()
    question_sql = session.query(Question).filter(Question.id == reply_sql.question_id).one()
    if question_sql.status is not 0:
        return False, msg.ERROR(1, "该问题已采纳！")
    question_sql.status = 1
    reply_sql.status = 1
    # 加钱
    user_sql = session.query(User).filter(User.id == user_id).one()
    user_sql.balance = user_sql.balance + question_sql.price
    session.commit()
    return True, msg.SUCCESS


@get_session
def report_reply_service(data):
    """

    :param data: {
        "id":123,
        "status": 2
    }
    :return:
    """
    session = g.session
    reply_sql = session.query(Reply).filter(Reply.id).one()
    reply_sql.status = data["status"]
    session.commit()