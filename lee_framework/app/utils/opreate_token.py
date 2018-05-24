#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/11/14 15:47
"""
import time, string, random
from jot import jwt, jws
from conf import web, ex_time
from db import redis_conn as redis_service


def en_token(telephone, user_id):
    iat = time.time()
    exp = iat + ex_time['token_ex']
    payload = {
        'telephone': str(telephone),
        'user_id': str(user_id),
        'iat': iat,
        'exp': exp
    }
    key_pix = generate_key()
    token = jwt.encode(payload, signer=jws.HmacSha(bits=256, key=web['token_key']+key_pix))
    redis_service.set(token, key_pix)
    return token


def de_token(token):
    if token is None:
        return None
    token = str(token)
    token_key_pix = redis_service.get(token)
    if token_key_pix is None:
        return None
    token_keys = web['token_key'] + token_key_pix
    no_valid_token = jwt.decode(token, signers=[jws.HmacSha(bits=256, key=token_keys)])
    if no_valid_token['valid']:
        return no_valid_token['payload']
    else:
        return None


def generate_key():
    """
    生成秘钥字符串
    :return:
    """
    base_str = string.digits + string.letters
    key_list = [random.choice(base_str) for i in range(web['key_len'])]
    key_str = "".join(key_list)
    return key_str
