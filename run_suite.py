"""
   组织测试套件实现 登录 与员工增删改查
"""
# 导包
import unittest
# 组织测试套件
from BeautifulReport import BeautifulReport

import app
from case.TestIHRMUser import TestUser
from case.testIHRMEmploye import TestEmployee

suite = unittest.TestSuite()
suite.addTest(TestUser("test_login_success")) #登录成功
suite.addTest(TestEmployee("test_emp_add"))
suite.addTest(TestEmployee("test_emp_update"))
suite.addTest(TestEmployee("test_emp_get"))
suite.addTest(TestEmployee("test_emp_delete"))

# 执行测试套件
# runner = unittest.THMLTestRunner()
# runner.run(suite)
BeautifulReport(suite).report(filename="report.html", description="IHRM",
                              log_path=app.PRO_PATH + "/report")
