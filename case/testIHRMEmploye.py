"""
    测试员工增删改查相关接口
"""
import requests
import unittest

import time

import app
from api.EmpAPL import EmpCRUD


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.session = requests.Session()
        self.emp_obj = EmpCRUD()

    def tearDown(self):
        self.session.close()

    # 测试函数:增
    def test_emp_add(self):
        # 1.请求业务
        response = self.emp_obj.add(self.session, "hahaha{}".format(time.strftime("%d%H%M%S")), "1531008{}".format(time.strftime("%d%H%M%S")), "65432100")
        # 2.断言业务
        print("新增成功响应结果:", response.json())

    # 测试函数:改
    def test_emp_update(self):
        # 请求业务
        response = self.emp_obj.update(self.session,
                                       "1184434491330220032",
                                       "hahaha1234868")
        # 断言业务
        print("修改后的响应体:", response.json())
        self.assertEqual(True, response.json().get("success"))

    # 测试函数:查
    def test_emp_get(self):
        # 1.请求业务
        response = self.emp_obj.get(self.session,"1184434491330220032")
        # 2.断言
        print("查询到的用户信息:",response.json())
        self.assertEqual(10000,response.json().get("code"))


    # 测试函数:删
    def test_emp_delete(self):
        # 1.请求业务
        response = self.emp_obj.delete(self.session, "1184434491330220032")
        # 2.断言
        print("删除的响应结果:", response.json())
        self.assertIn("操作成功", response.json().get("message"))
