#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/11/14 9:54
"""
from flask import g
from lib.flask import app
from lib.utils import err_ret
from msg import msg


@app.teardown_request
def teardown_request(exception):
    print exception
    try:
        pass
        # g.session.rollback()
        # g.session.close()
    except:
        pass

    return err_ret(msg.ERROR(500, exception))