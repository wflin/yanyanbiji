#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/11/14 9:59
"""
from app import app

from lib.utils import package_import


package_import("app.views")
package_import("lib.errors")
package_import("intercept")
package_import("intercept.before_request")
