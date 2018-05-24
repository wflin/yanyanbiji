#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/12/15 15:07
"""
from datetime import datetime
from flask import g

from app.models.report import Report
from app.utils.get_info import get_session


@get_session
def add_report(data):
    """
    添加举报
    :param data: {
        "des":"",
        "type":"",
        "record_id":""
    }
    :return:
    """
    session = g.session
    report = Report(des=data["des"], type=data["type"], record_id=data["record_id"], create_time=datetime.now())
    session.add(report)
    session.commit()


@get_session
def list_report(data):
    """
    举报查询
    :param data:{
        "type": 0  # 类型 0 产品 1 问题 2 回复
        "limit":9,
        "page":9
    }
    :return:
    """
    session = g.session
    # 分页
    limit = data['limit']
    offset = (data['page'] - 1) * data['limit']
    sql_result = session.query(Report).filter(Report.type == data["type"])
    total = sql_result.count()
    sql_content = sql_result.order_by(Report.create_time.desc()).limit(limit).offset(offset)
    items = [i.to_json() for i in sql_content]
    return True, items, total