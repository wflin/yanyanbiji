# encoding: utf-8

"""
@author: leason
@time: 2017/11/14 11:01
"""


class ERROR(object):
    def __init__(self, code, msg, err_code=0):
        self.code = code
        self.msg = msg
        self.err_code = err_code


# global params
SUCCESS = ERROR(0, u"操作成功")
FAIL = ERROR(1, u"操作失败")
PARAMS_ERR = ERROR(1001, u"请求参数不合法")
INVALID_REQUEST = ERROR(1002, u"请求已过期")

# sms_code
A_MAX_REQUEST = ERROR(2001, u"请求频繁，稍后再试")
A_SMS_ERR = ERROR(2002, u"请求频繁，稍后再试")
A_CODE_ERR = ERROR(2003, u"验证码错误")
A_CODE_TIMEOUT = ERROR(2004, u"验证码已失效")

# register
A_EXIST = ERROR(4001, u"该账户已经注册")
A_PWD_ERR = ERROR(4002, u"两次密码不一致")
A_LOGIN_ERR = ERROR(4003, u"用户名或密码错误")
A_NO_EXIST = ERROR(4004, u"用户不存在")
A_LOGIN_MAX = ERROR(4005, u"用户或密码达到错误次数达到最大上限，冻结用户10分钟")
A_DISABLED = ERROR(4006, u"账号已被禁用")
A_SIGNED = ERROR(4008, u"账号已在其他地方登录")
A_TIMEOUT = ERROR(4008, u"登录失效")
A_NO_AUTHOR = ERROR(4009, u"无权限")

# 登录
LOGIN_SUCCESS = ERROR(0, u"登录成功")
LOGOUT_SUCCESS = ERROR(0, u"注销成功")