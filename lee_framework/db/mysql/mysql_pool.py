#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/11/14 14:35
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, exc
from sqlalchemy.pool import QueuePool
from lib.utils import logging, package_import
from conf import mysql_pool_configs, switch


def engine():
    db_pool = None
    try:
        db_pool = create_engine(mysql_pool_configs['url'], poolclass=QueuePool,
                                pool_size=mysql_pool_configs['pool_size'],
                                max_overflow=mysql_pool_configs['max_overflow'],
                                pool_recycle=mysql_pool_configs['pool_recycle'],
                                echo=False
                                )
    except exc.OperationalError as e:
        logging.debug("create pool err:", e)
    return db_pool
mysql_engine = engine()
ModelBase = declarative_base()

if switch['create_table']:
    package_import("app.models")

    ModelBase.metadata.create_all(bind=mysql_engine)

