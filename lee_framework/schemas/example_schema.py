# encoding: utf-8

"""
@author: leason
@time: 2017/11/14 9:55
"""
from lib.schemas import app_schema_request

# 这个例子将对接口 /login 的请求json进行校验
# 如需将规则分别添加到不同的文件 直接在该目录下新建py文件然后仿照该例子添加规则即可
app_schema_request['/login'] = {
    "opr": {
        "type": "string",
        "enum": ["collection", "pay_for"]
    }
}
