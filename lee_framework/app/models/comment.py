#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/12/15 21:32
"""
from sqlalchemy import Column, Integer, String, Text, DateTime
from db.mysql.mysql_pool import ModelBase
from lib.utils.common import date_time


# 评论表
class Comment(ModelBase):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True, autoincrement=True) # id
    create_time = Column(DateTime)                             # 创建时间
    user_name = Column(String(length=50), default="")          # 用户名称
    user_id = Column(Integer, default=0)                       # 用户id
    content = Column(Text, default="")                         # 评论内容
    product_id = Column(Integer)                               # 资料id
    pic = Column(String(length=500), default="")               # 图片
    real_star = Column(Integer, default=0)                     # 如实描述0-5
    price_star = Column(Integer, default=0)                    # 性价比0-5
    clean_star = Column(Integer, default=0)                    # 干净指数0-5
    average_star = Column(Integer)                             # 平均分
    status = Column(Integer, default=0)                        # 0正常评论 1违规评论

    def __init__(self):
        self.create_time = date_time()
        self.status = 0

    def to_json(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "user_id": self.user_id,
            "content": self.content,
            "product_id": self.product_id,
            "status": self.status,
            "pic": self.pic,
            "real_star": self.real_star,
            "price_star": self.price_star,
            "clean_star": self.clean_star,
            "average_star": self.average_star,
            "create_time": str(self.create_time)
        }