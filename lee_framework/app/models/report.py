#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2018/1/30 19:32
"""
# 举报表
from sqlalchemy import Integer, Column, String, DateTime

from db.mysql.mysql_pool import ModelBase


class Report(ModelBase):
    __tablename__ = "report"

    id = Column(Integer, primary_key=True, autoincrement=True)        # id
    type = Column(Integer, default=0)                                 # 类型 0 产品 1 问题 2 回复
    des = Column(String(length=255), default="")                      # 举报描述
    record_id = Column(Integer)                                       # 举报记录的id
    create_time = Column(DateTime)                                    # 创建时间

    def to_json(self):
        return {
            "id": self.id,
            "type": self.type,
            "des": self.des,
            "record_id": self.record_id,
            "create_time": str(self.create_time)
        }


