#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/12/15 14:32
"""
from sqlalchemy import Column, Integer, String, Text, DateTime
from db.mysql.mysql_pool import ModelBase
from lib.utils.common import date_time


# 产品表
class Product(ModelBase):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, autoincrement=True) # id
    create_time = Column(DateTime)                             # 创建时间
    name = Column(String(length=50), default="")               # 资料名称
    describe = Column(String(length=500), default="")          # 资料描述
    detail = Column(Text, default="")                          # 详情
    publisher_id = Column(Integer)                             # 发布人id
    type = Column(Integer)                                     # 资料类型   0纸质资料 1下载资料
    pic = Column(String(length=500), default="")               # 图片
    logistics_price = Column(Integer, default=0)               # 图片资料运费
    price = Column(Integer, default=0)                         # 资料价格 单位分
    status = Column(Integer, default=0)                        # 0 上架
    category = Column(String(length=500), default="")          # 类别

    def __init__(self):
        self.create_time = date_time()
        self.status = 0

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "describe": self.describe,
            "detail": self.detail,
            "type": self.type,
            "status": self.status,
            "category": self.category,
            "pic": self.pic,
            "price": self.price,
            "logistics_price": self.logistics_price,
            "create_time": str(self.create_time)
        }


# 问题表
class Question(ModelBase):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True, autoincrement=True)  # id
    create_time = Column(DateTime)  # 创建时间
    name = Column(String(length=50), default="")  # 问题名称
    detail = Column(Text, default="")  # 详情
    publisher_id = Column(Integer)  # 提问人id
    price = Column(Integer, default=0)  # 资料价格 单位分
    status = Column(Integer, default=0)  # 0 正常 1 已完成采纳 2违规
    category = Column(String(length=500), default="")  # 类别

    def __init__(self):
        self.create_time = date_time()
        self.status = 0

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "detail": self.detail,
            "status": self.status,
            "publisher_id": self.publisher_id,
            "category": self.category,
            "price": self.price,
            "create_time": str(self.create_time)
        }


# 回复表
class Reply(ModelBase):
    __tablename__ = "reply"

    id = Column(Integer, primary_key=True, autoincrement=True)  # id
    create_time = Column(DateTime)  # 创建时间
    content = Column(Text, default="")  # 详情
    reply_id = Column(Integer)  # 回答人id
    question_id = Column(Integer)  # 问题id
    status = Column(Integer, default=0)  # 0 正常 1 已被采纳 2违规
    thumbs_num = Column(Integer, default=0)  # 点赞数量
    thumbs_user = Column(Text, default="")  # 点赞用户id 多用户“，”隔开

    def __init__(self):
        self.create_time = date_time()
        self.status = 0

    def to_json(self):
        return {
            "id": self.id,
            "content": self.content,
            "status": self.status,
            "reply_id": self.reply_id,
            "question_id": self.question_id,
            "thumbs_num": self.thumbs_num,
            # "thumbs_user": self.thumbs_user,
            "create_time": str(self.create_time)
        }
