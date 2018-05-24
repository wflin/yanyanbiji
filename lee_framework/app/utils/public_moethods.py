#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/11/15 14:06
"""
import random


def generate_code():
    """
    生成6位短信验证码
    :return:
    """
    random_seeds = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    str_slice = random.sample(random_seeds, 6)
    sms_code = ''.join(str_slice)
    return sms_code