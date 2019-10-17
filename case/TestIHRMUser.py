"""
    测试用户模块实现
            登录接口    
    参数化实现回顾
        1.导包
        2.设置
        3.解析
"""
# 导包
import json
import unittest
import requests
from parameterized import parameterized

#填写json 解析函数
import app
from api.UserAPI import Userlogin


def read_json():
    # 1.创建
    data = []
    # 2.打开文件
    with open(app.PRO_PATH + "/data/login_data.json","r",encoding="utf-8")as f:
        for value in json.load(f).values():
            mobile = value.get("mobile")
            password = value.get("password")
            success = value.get("success")
            code = value.get("code")
            message = value.get("message")
            ele = (mobile,password,success,code, message)
            data.append(ele)
    # 3.返回
    return data


# 创建测试类(继承 TestCase)
class TestUser(unittest.TestCase):
    # 初始化函数
    def setUp(self):
        # 初始化session
        self.session = requests.Session()
        # 初始化 ipa 对象
        self.user_login=Userlogin()
    # 资源销毁函数
    def tearDown(self):
        # 销毁 session
        self.session.close()

    # 测试函数:登录
    # 使用参数化
    @parameterized.expand(read_json)
    def test_login(self,mobile,password,success,code, message):
        print("-"*100)
        print(mobile, password, success, code, message)
        # 1.调用请求业务
        # response = 初始化apidx对象.登录
        response = self.user_odj.login(self.session,mobile, password, success, code, message)
        # 2.调用断言业务
        print(response.json())
        result = response.json()


    # 测试函数:
    def test_login_success(self):
        print("-"*100)

        print("登录成功接口")
        # 1.请求业务
        response = self.user_login.login(self.session,"13800000002","123456")
        # 2.断言业务
        result = response.json()
        print("登录成功的响应结果")
        self.assertEqual(True, result.get("success"))
        self.assertEqual(10000, result.get("code"))
        self.assertIn("操作成功", result.get("message"))
        # 提取 token值
        token =result.get("data")
        print("登录成功后的 token 值:", token)
        app.TOKEN = token # 变局部变量为全局变量