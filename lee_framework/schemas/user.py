#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/11/14 9:55
"""

from lib.schemas import app_schema_request


app_schema_request['/user/login'] = {
    'telephone': {'type': 'string'},
    'password': {'type': 'string'}
}