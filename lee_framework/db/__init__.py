#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/11/14 14:11
"""
from mysql.mysql_pool import mysql_engine
from sqlalchemy.orm import sessionmaker

from redis.redis_pool import redis_engine

session_factory = sessionmaker(bind=mysql_engine)
redis_conn = redis_engine()