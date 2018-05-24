#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/12/15 15:07
"""
from flask import g
from sqlalchemy import and_, or_

from app.models.chat import Chat, ChatList
from app.models.user_models import User
from app.utils.get_info import get_session, get_user_info
from msg import msg


@get_session
def add_chat_service(data):
    """
    发消息
    :param data:{
        # "send_id": "",
        "get_id": "",
        "content": ""
    }
    :return:
    """
    session = g.session
    data["send_id"] = get_user_info()["user_id"]
    if int(data["send_id"]) == int(data["get_id"]):
        return 2
    chat = Chat()
    for key, value in data.items():
        setattr(chat, key, value)
    # 标记接受者新消息
    sql_result = session.query(ChatList).filter(
        and_(
            ChatList.get_id == data["get_id"],
            ChatList.send_id == data["send_id"]
        )

    ).one_or_none()
    if sql_result:
        sql_result.status = 0
    else:
        chat_list = ChatList()
        chat_list.send_id = data["send_id"]
        chat_list.get_id = data["get_id"]
        chat_list.status = 0
        session.add(chat_list)
    session.add(chat)
    session.commit()
    return True


@get_session
def list_chat_service(data):
    """
    查询聊天消息
    :param data: {
        # "user_id":451
        "send_id":451
        "get_id":451
        "limit": 8,
        "page": 1
    }
    :return:
    """
    session = g.session
    # 分页
    limit = data['limit']
    offset = (data['page'] - 1) * data['limit']

    sql_result = session.query(Chat).filter(
        or_(
            and_(
                Chat.get_id == data["get_id"],
                Chat.send_id == data["send_id"]
            ),
            and_(
                Chat.get_id == data["send_id"],
                Chat.send_id == data["get_id"]
            )
        )

    )
    total = sql_result.count()
    sql_content = sql_result.order_by(Chat.create_time).limit(limit).offset(offset)
    result = []
    for i in sql_content:
        c = i.to_json()
        sql_send = session.query(User).filter(User.id == i.send_id).one()
        sql_get = session.query(User).filter(User.id == i.get_id).one()
        c["send_user"] = sql_send.to_json()
        c["get_user"] = sql_get.to_json()
        # type为1收 0 发
        c["type"] = 1
        if c["send_id"] == int(data["user_id"]):
            c["type"] = 0
        result.append(c)

    return True, result, total


@get_session
def status_chat_service(data):
    """
    有无新消息
    :param data:{
        # "user_id":451
        "limit": 8,
        "page": 1
    }
    :return:
    """
    session = g.session
    user_id = get_user_info()["user_id"]
    # 分页
    limit = data['limit']
    offset = (data['page'] - 1) * data['limit']

    sql_result = session.query(ChatList).filter(ChatList.get_id == user_id)
    total = sql_result.count()
    sql_content = sql_result.order_by(ChatList.create_time.desc()).limit(limit).offset(offset)
    result = []
    for i in sql_content:
        c = i.to_json()
        sql_send = session.query(User).filter(User.id == i.send_id).one()
        sql_get = session.query(User).filter(User.id == i.get_id).one()
        c["send_user"] = sql_send.to_json()
        c["get_user"] = sql_get.to_json()
        result.append(c)

    return True, result, total