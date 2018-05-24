#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/11/14 9:55
"""
from flask_cors import CORS
from lib.flask import app
from lib.schemas import app_schema_config
from lib.validator import JValidator
from conf import *


def check_config():
    validator = JValidator(app_schema_config)
    for configs in validator.schema.keys():
        from lib.exception import ConfigError

        correct, err = validator.validate(eval(configs), configs)
        if not correct:
            raise ConfigError(config_name=configs, err=err)

if __name__ == '__main__':
    """
    app.debug=True时，定时任务或其他脚本会被执行了2次，原因是flask会多开一个线程来监测项目的变化
    解决方案可以将app.dubug修改为False或添加参数use_reloader=False
    """
    check_config()
    if web['debug']:
        CORS(app, supports_credentials=True)
        app.run(host=web['ip'], port=web['port'], debug=True,threaded=True)
    else:
        app.run(host=web['ip'], port=web['port'])