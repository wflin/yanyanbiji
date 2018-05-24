#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/12/15 21:32
"""
from sqlalchemy import Column, Integer, String, DateTime
from db.mysql.mysql_pool import ModelBase
from lib.utils.common import date_time


# 订单表
class Order(ModelBase):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, autoincrement=True)  # id
    order_num = Column(String(length=50), default="")           # 订单编号
    status = Column(Integer, default=0)                         # 0 未发货 1 已发货 2 确认收货 3 交易关闭
    create_time = Column(DateTime)                              # 创建时间
    buyer_id = Column(Integer, default=0)                       # 买家id
    seller_id = Column(Integer, default=0)                      # 卖家id
    logistics_num = Column(String(length=50), default="")       # 快递单号
    product_num = Column(Integer, default=1)                    # 购买数量
    product_id = Column(Integer, default=0)                     # 产品id
    product_amount = Column(Integer, default=0)                 # 商品总额
    logistics_amount = Column(Integer, default=0)               # 快递总额


    def __init__(self):
        self.create_time = date_time()
        self.status = 0

    def to_json(self):
        return {
            "id": self.id,
            "order_num": self.order_num,
            "create_time": str(self.create_time),
            "buyer_id": self.buyer_id,
            "seller_id": self.seller_id,
            "logistics_num": self.logistics_num,
            "product_num": self.product_num,
            "product_id": self.product_id,
            "product_amount": self.product_amount,
            "logistics_amount": self.logistics_amount
        }