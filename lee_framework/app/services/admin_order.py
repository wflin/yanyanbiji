#!/usr/bin/env python
# encoding: utf-8
from flask import g
from sqlalchemy import and_

from app.models.order import Order
from app.models.product import Product
from app.models.user_models import User
from app.utils.get_info import get_session


@get_session
def list_order_admin(data):
    """
    查询订单
    :param data: {
        "cond":{
            "product_name": "sd", #书籍名称
            "start_time": "2017-12-19",
            "end_time": "2017-12-19",
            "status":0  #订单状态
        },
        "limit":8,
        "page":0
    }
    :return:
    """
    session = g.session
    # 分页
    limit = data['limit']
    offset = (data['page'] - 1) * data['limit']

    cond = data["cond"]

    result_sql = session.query(Order, Product).filter(Order.status.like('%' + str(cond['status']) + '%') if cond['status'] is not None else "").join(
        Product, and_(
            Order.product_id == Product.id,
            Order.create_time.between(cond["start_time"], cond["end_time"]) if cond['start_time'] != "" else "",
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
def status_order_admin(data):
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