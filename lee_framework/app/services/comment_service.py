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
def add_comment_service(data):
    """
    添加评价
    :param data:
    {
        # "user_name": self.user_name,
        # "user_id": self.user_id,
        "content": self.content,
        "product_id": self.product_id,
        "pic": self.pic,
        "real_star": self.real_star,
        "price_star": self.price_star,
        "clean_star": self.clean_star,
    }
    :return:
    """
    session = g.session
    result = session.query(User).filter(User.id == data["user_id"]).one()
    data["user_name"] = result.username
    data["average_star"] = (data["real_star"] + data["price_star"] + data["clean_star"])/3
    comment = Comment()
    for key, value in data.items():
        setattr(comment, key, value)
    session.add(comment)
    session.commit()
    return True


@get_session
def delete_comment_service(comment_id, user_id):
    """
    删除评论
    :param comment_id: 评论id
    :param user_id: 用户id
    :return:
    """
    session = g.session
    product = session.query(Comment).filter(Comment.id == comment_id).filter(Comment.user_id == user_id).one_or_none()
    if product:
        session.delete(product)
        session.commit()
        return True
    return False


@get_session
def list_comment_service(data):
    """
    查询某个产品的评论
    :param data: {
        "product_id":451，
        "limit": 8,
        "page": 1
    }
    :return:
    """
    session = g.session
    # 分页
    limit = data['limit']
    offset = (data['page'] - 1) * data['limit']
    if data.get("product_id"):
        sql_result = session.query(Comment).filter(Comment.product_id == data["product_id"])
    else:
        sql_result = session.query(Comment).filter(Comment.user_id == data["user_id"])
    total = sql_result.count()
    sql_content = sql_result.order_by(Comment.create_time.desc()).limit(limit).offset(offset)
    result = [i.to_json() for i in sql_content]

    return True, result, total