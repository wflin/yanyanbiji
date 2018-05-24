#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/11/14 14:12
"""
"""
系统全局配置文件
"""
db_type = {
    "mysql": "mysql",
    "redis": "redis"
}

# 一些开关
switch = {
    # "create_table": True
    "create_table": False
}
# web
web = {
    "url_pre": "/api/yan",
    "api_version": ["v1"],
    "ip": "0.0.0.0",
    "port": 8082,
    "debug": True,
    "root": True,
    "token_key": "leeFrameWork",
    "key_len": 8,
    "pic_pix": "/static_file/",
    "upload_path": "/usr/share/nginx/html/static_file/uploads"
}

mysql_pool_configs = {
    "url": "mysql+pymysql://yanyan:050078@106.14.9.214:3306/yanyan?charset=utf8",
    "pool_size": 1,
    "max_overflow": 10,
    "pool_recycle": 2*60*60

}

redis_pool_configs = {
        "type": db_type["redis"],
        "host": "106.14.9.214",
        "port": 6379,
        "pool_size": 5, # 0表示不使用连接池 最大连接数
        "user_name": "",
        "password": "",
        "db_name": "yanyan"
}


# 日志配置
log = {
    "name": "leeFrameWork",
    "level": "debug",
    "console": True,
    "format": "%(thread)d:%(asctime)s %(funcName)s:%(lineno)d %(filename)s - %(name)s %(levelname)s - %(message)s",
    "file": {
        "enable": False,
        "path": ""
    },
    "syslog": {
        "enable": True,
        "ip": "127.0.0.1",
        "port": 10514,
        "facility": "local5"
    }
}

sqltime_log_config = {
    "name": "sqltime",
    "level": "debug",
    "console": False,
    "format": "%(asctime)s %(funcName)s:%(lineno)d %(filename)s - %(name)s %(levelname)s - %(message)s",
    "file": {
        "enable": False,
        "path": ""
    },
    "syslog": {
        "enable": True,
        "ip": "127.0.0.1",
        "port": 10514,
        "facility": "local5"
    }
}

pool_log_config = {
    "name": "sqlalchemy.pool",
    "level": "debug",
    "console": False,
    "format": "%(asctime)s %(funcName)s:%(lineno)d %(filename)s - %(name)s %(levelname)s - %(message)s",
    "file": {
        "enable": False,
        "path": ""
    },
    "syslog": {
        "enable": True,
        "ip": "127.0.0.1",
        "port": 10514,
        "facility": "local5"
    }
}
# 邮件
email = {
    "smtp_addr": "smtp.qq.com",
    "from_email": "446330342@qq.com",
    "from_email_pwd": "vibwzctxgecpbhba",
    "subject": "邮箱验证"
}


# 注册短信验证码配置参数
R_SMS = {
    # 秘钥ID
    "ACCESS_KEY_ID": "LTAIc7ywZbHzOVQb",
    "ACCESS_KEY_SECRET": "HDxkYP1ZhDJN8BRXIK3hEHJyQEF3Tw",
    "template_code": "SMS_121906365",
    "sign_name": u"研研笔记",
    "template_string": "code",
    "redis_timeout": 5*60
}

# redis前缀
redis_pre = {
    # token
    'token_pix': 't_pix_',
    # sms
    'register_sms': 'r_sms_',
    # 访问控制
    'access_pix': 'a_pix_'
}

# redis有效时间配置
ex_time = {
    # token
    'token_ex': 10*24*60*60,
    # 访问控制
    'access_ex': 1
}