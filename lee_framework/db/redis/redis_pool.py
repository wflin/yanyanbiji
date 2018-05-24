#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/11/14 14:35
"""
import redis

from conf import redis_pool_configs

redis_config = redis_pool_configs


def redis_engine():
    configs = dict()
    configs['host'] = redis_config['host']
    configs['port'] = redis_config['port']
    configs['max_connections'] = redis_config['pool_size']
    pool = redis.ConnectionPool(**configs)
    if redis_config['password'] == '':
        r = redis.StrictRedis(connection_pool=pool)
    else:
        r = redis.StrictRedis(connection_pool=pool, password=redis_config['password'])
    return r
