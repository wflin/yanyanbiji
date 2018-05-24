#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2018/1/2 21:07
"""
from flask import g
from sqlalchemy import and_, or_

from app.models.comment import Comment
from app.models.product import Product
from app.models.user_models import User
from app.models.order import Order
from app.utils.get_info import get_session, get_user_info
from lib.utils.common import date_time, to_list
from msg import msg


@get_session
def add_order_service(data):
    """
    生成订单
    :param data:[
        {
            "product_id": 78, # 产品id
            "product_num": 2, # 产品数量
        }
    ]
    :return:
    """
    session = g.session
    user_id = get_user_info()["user_id"]
    for item in to_list(data):
        result = session.query(Product).filter(Product.id == item["product_id"]).one()
        order = Order()
        order.order_num = date_time(fmt="%Y%m%d%H%M%S") + str(user_id) + str(item["product_id"])
        order.product_id = item["product_id"]
        order.buyer_id = user_id
        order.seller_id = result.publisher_id
        order.product_num = item["product_num"]
        order.product_amount = item["product_num"]*result.price
        order.logistics_amount = result.logistics_price
        session.add(order)

    session.commit()
    return True


@get_session
def list_order_service(data):
    """
    查询订单
    :param data: {
        "cond":{
            "type":"buy", # buy 购买 sell 出售
            "product_name": "sd", #书籍名称
            "status":0  #订单状态
        },
        "limit":8,
        "page":0
    }
    :return:
    """
    session = g.session
    buy_id = None
    sell_id = None
    if data["cond"]["type"] == "buy":
        buy_id = get_user_info()["user_id"]
    else:
        sell_id = get_user_info()["user_id"]
    # 分页
    limit = data['limit']
    offset = (data['page'] - 1) * data['limit']

    cond = data["cond"]

    result_sql = session.query(Order, Product).filter(Order.status.like('%' + str(cond['status']) + '%') if cond['status'] is not None else "").join(
        Product, and_(
            Order.product_id == Product.id,
            Order.buyer_id == buy_id if buy_id is not None else "",
            Order.seller_id == sell_id if sell_id is not None else "",
            Product.name.like('%' + str(cond['product_name']) + '%') if cond['product_name'] is not None else ""
        ))
    total = result_sql.count()
    sql_content = result_sql.order_by(Order.create_time.desc()).limit(limit).offset(offset)
    items = []
    for i in sql_content:
        c = dict()
        c["order"] = i[0].to_json()
        c["product"] = i[1].to_json()
        sql_seller = session.query(User).filter(User.id == i[0].seller_id).one()
        sql_buyer = session.query(User).filter(User.id == i[0].buyer_id).one()
        c["seller"] = sql_seller.to_json()
        c["buyer"] = sql_buyer.to_json()
        items.append(c)
    return True, items, total


@get_session
def deliver_order_service(data):
    """
    发货
    :param data:{
        "id":8,
        "logistics_num":44545
    }
    :return:
    """
    session = g.session
    order_sql = session.query(Order).filter(Order.id == data.pop("id")).one_or_none()
    order_sql.logistics_num = data["logistics_num"]
    session.commit()
    return True


@get_session
def status_order_service(data):
    """
    修改订单状态
    :param data:{
        "id":45,
        "status": 3
    }
    :return:
    """
    session = g.session
    order_sql = session.query(Order).filter(Order.id == data.pop("id")).one_or_none()
    order_sql.status = data["status"]
    session.commit()
    return True


@get_session
def detail_order_service(order_id):
    """
    订单详情
    :param order_id:
    :return:
    """
    session = g.session
    result_sql = session.query(Order, Product).join(
        Product, and_(
            Order.product_id == Product.id,
            Order.id == order_id
        )).one()

    c = dict()
    c["order"] = result_sql[0].to_json()
    c["product"] = result_sql[1].to_json()
    sql_seller = session.query(User).filter(User.id == result_sql[0].seller_id).one()
    sql_buyer = session.query(User).filter(User.id == result_sql[0].buyer_id).one()
    c["seller"] = sql_seller.to_json()
    c["buyer"] = sql_buyer.to_json()
    return c