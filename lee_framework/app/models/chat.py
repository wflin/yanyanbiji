#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2018/01/08 21:32
"""
from sqlalchemy import Column, Integer, String, Text, DateTime
from db.mysql.mysql_pool import ModelBase
from lib.utils.common import date_time


# 聊天记录表
class Chat(ModelBase):
    __tablename__ = "chat"

    id = Column(Integer, primary_key=True, autoincrement=True)  # id
    create_time = Column(DateTime)                              # 创建时间
    send_id = Column(Integer, default=0)                        # 发送id
    get_id = Column(Integer, default=0)                         # 接收id
    content = Column(Text, default="")                          # 消息内容

    def __init__(self):
        self.create_time = date_time()

    def to_json(self):
        return {
            "id": self.id,
            "send_id": self.send_id,
            "get_id": self.get_id,
            "content": self.content,
            "create_time": str(self.create_time)
        }


# 聊天记录列表 表
class ChatList(ModelBase):
    __tablename__ = "chat_list"

    id = Column(Integer, primary_key=True, autoincrement=True)  # id
    create_time = Column(DateTime)                              # 创建时间
    get_id = Column(Integer, default=0)                         # 接收id
    send_id = Column(Integer, default=0)                         # 接收id
    status = Column(Integer, default=0)                         # 0新消息 1无新消息

    def __init__(self):
        self.create_time = date_time()
        self.status = 0

    def to_json(self):
        return {
            "id": self.id,
            "get_id": self.get_id,
            "send_id": self.send_id,
            "status": self.status,
            "create_time": str(self.create_time)
        }