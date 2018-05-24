#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/12/15 15:07
"""
from datetime import datetime
from flask import g
from sqlalchemy import and_, or_

from app.models.carousel import Carousel
from app.utils.get_info import get_session


@get_session
def add_carousel(data):
    """
    添加轮播图
    :param data: {
        "des":"",
        "pic":""
    }
    :return:
    """
    session = g.session
    carousel = Carousel(des=data["des"], pic=data["pic"], create_time=datetime.now())
    session.add(carousel)
    session.commit()


@get_session
def list_carousel(data):
    """
    轮播图查询
    :param data:{
        "limit":9,
        "page":9
    }
    :return:
    """
    session = g.session
    # 分页
    limit = data['limit']
    offset = (data['page'] - 1) * data['limit']
    sql_result = session.query(Carousel)
    total = sql_result.count()
    sql_content = sql_result.order_by(Carousel.create_time.desc()).limit(limit).offset(offset)
    items = [i.to_json() for i in sql_content]
    return True, items, total


@get_session
def delete_carousel(carousel_id):
    """
    删除轮播图
    :param carousel_id:
    :return:
    """
    session = g.session
    carousel = session.query(Carousel).filter(Carousel.id == carousel_id).one_or_none()
    if carousel:
        session.delete(carousel)
        session.commit()
        return True
    return False
