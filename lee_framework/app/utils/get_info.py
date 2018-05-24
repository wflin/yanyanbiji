#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/11/15 14:06
"""
from flask import request, g
from db import session_factory
import json


# 获取请求参数
def get_params():
    """
    获取请求参数
    before_request已经格式化
    :return: dict
    """
    params = getattr(request, "params")

    return params


# 获取请求参数
def get_user_info():
    """
    获取用户信息
    :return: dict
    """
    return g.user_info


# 获取数据库session装饰器
def get_session(func):
    """
    获取数据库session
    :return:
    """
    def inner(*args, **kwargs):
        g.session = session_factory()
        return func(*args, **kwargs)
    return inner
