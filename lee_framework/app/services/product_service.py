#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/12/15 15:07
"""
from flask import g
from sqlalchemy import and_, or_

from app.models.comment import Comment
from app.models.product import Product
from app.models.user_models import User
from app.utils.get_info import get_session
from msg import msg


@get_session
def add_product_service(data):
    """
    添加资料
    :param data:{
        "name": self.name,
        "describe": self.describe,
        "detail": self.detail,
        "type": self.type,
        "pic": self.pic,
        "category": category,
        "price": self.price
    }
    :return:
    """
    session = g.session
    product = Product()
    for key, value in data.items():
        setattr(product, key, value)
    session.add(product)
    session.commit()
    return True


@get_session
def modify_product_service(data):
    """
    编辑资料 或者 下架商品
    :param data:{
        "id":465464,
        "name": self.name,
        "describe": self.describe,
        "detail": self.detail,
        "type": self.type,
        "pic": self.pic,
        "category": category,
        "price": self.price
    }
    :return:
    """
    session = g.session
    product_sql = session.query(Product).filter(Product.id == data.pop("id")).one_or_none()
    if product_sql:
        for key, value in data.items():
            # print key, value
            setattr(product_sql, key, value)

        session.commit()

        return True
    return False


@get_session
def delete_product_service(product_id):
    """
    删除商品
    :param product_id:
    :return:
    """
    session = g.session
    product = session.query(Product).filter(Product.id == product_id).one_or_none()
    if product:
        session.delete(product)
        session.commit()
        return True
    return False


@get_session
def list_product_service(data):
    """
    用户查询发布的产品
    :param data: {
        "user_id":451
        "limit": 8,
        "page": 3

    }
    :return:
    """
    session = g.session
    # 分页
    limit = data['limit']
    offset = (data['page'] - 1) * data['limit']

    sql_result = session.query(Product).filter(Product.publisher_id == data["user_id"])
    total = sql_result.count()
    sql_content = sql_result.order_by(Product.create_time.desc()).limit(limit).offset(offset)
    result = [i.to_json() for i in sql_content]

    return True, result, total


@get_session
def all_product_service(data):
    """
    查询所有资料
    :param data: {
        "cond":{
            "id": 123,
            "key_word": "sd",
            "type":0,
            "category":0
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
    result_sql = session.query(Product, User).join(
        User, and_(
            Product.publisher_id == User.id,
            Product.status == 0,
            Product.id == cond['id'] if cond.get("id") is not None else "",
            Product.type.like('%' + str(cond['type']) + '%') if cond['type'] is not None else "",
            Product.category.like('%' + str(cond['category']) + '%') if cond['category'] is not None else "",
            or_(
                Product.name.like('%' + str(cond['key_word']) + '%') if cond['key_word'] is not None else "",
                Product.describe.like('%' + str(cond['key_word']) + '%') if cond['key_word'] is not None else "",
            )

        ))
    total = result_sql.count()
    sql_content = result_sql.order_by(Product.create_time.desc()).limit(limit).offset(offset)
    items = []
    for i in sql_content:
        c = dict()
        c["product"] = i[0].to_json()
        c["user"] = i[1].to_json()
        sql_comment = session.query(Comment).filter(Comment.product_id == i[0].id)
        c["comment_num"] = sql_comment.count()
        c["average_star"] = 0
        if c["comment_num"]:
            c["average_star"] = sum([a.average_star for a in sql_comment])/int(c["comment_num"])
        items.append(c)
    return True, items, total


@get_session
def detail_product_service(product_id):
    """
    资料id
    :param product_id:
    :return:
    """
    session = g.session
    result_sql = session.query(Product, User).join(
        User, and_(
            Product.publisher_id == User.id,
            Product.id == product_id
        )).one()
    c = dict()
    c["product"] = result_sql[0].to_json()
    c["user"] = result_sql[1].to_json()
    sql_comment = session.query(Comment).filter(Comment.product_id == result_sql[0].id)
    c["comment_num"] = sql_comment.count()
    c["average_star"] = 0
    if c["comment_num"]:
        c["average_star"] = sum([a.average_star for a in sql_comment])/int(c["comment_num"])
    return c