#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2018/1/30 19:32
"""
# 轮播图表
from sqlalchemy import Integer, Column, String, DateTime

from db.mysql.mysql_pool import ModelBase


class Carousel(ModelBase):
    __tablename__ = "carousel"

    id = Column(Integer, primary_key=True, autoincrement=True)        # id
    type = Column(Integer, default=0)                                 # 类型 0 id
    enable = Column(Integer, default=0)                               # 启用禁言 0 启用 1禁用
    des = Column(String(length=255), default="")                      # 描述
    pic = Column(String(length=255), default="")                      # 图片地址
    params = Column(String(length=255), default="")                   # 参数图片地址
    create_time = Column(DateTime)                                    # 创建时间

    def to_json(self):
        return {
            "id": self.id,
            "des": self.des,
            "pic": self.pic,
            "create_time": str(self.create_time)
        }