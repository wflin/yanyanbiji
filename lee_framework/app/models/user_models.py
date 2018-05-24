#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/11/15 14:32
"""
from sqlalchemy import Column, Integer, String, Enum, DateTime
from db.mysql.mysql_pool import ModelBase
from lib.utils.common import date_time


# 个体用户表
class User(ModelBase):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)              # id
    create_time = Column(DateTime, default="")                              # 创建时间
    telephone = Column(String(length=15), default="", unique=True)          # 绑定手机号
    password = Column(String(length=50), default="")                        # 登录密码
    pay_password = Column(String(length=50), default="")                        # 支付密码
    username = Column(String(length=20), default=u"用户xx")                        # 昵称
    school = Column(String(length=200), default="")                         # 学校
    address = Column(String(length=200), default="")                        # 地址
    pic = Column(String(length=200), default="")                            # 头像
    balance = Column(Integer, default=0)                                    # 余额

    def __init__(self, password, telephone, username=None):
        self.create_time = date_time()
        self.username = username
        self.password = password
        self.telephone = telephone

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "telephone": self.telephone,
            "balance": self.balance,
            "school": self.school,
            "address": self.address,
            "pic": self.pic,
            "create_time": str(self.create_time)
        }

    def admin_to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "telephone": self.telephone,
            "balance": self.balance,
            "school": self.school,
            "address": self.address,
            "pic": self.pic,
            "create_time": str(self.create_time)
        }


# 管理员表
class Admin(ModelBase):
    __tablename__ = "admin"

    id = Column(Integer, primary_key=True, autoincrement=True)        # id
    username = Column(String(length=200), default="")                 # 账号
    password = Column(String(length=200), default="")                 # 密码