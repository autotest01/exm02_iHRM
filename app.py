"""
    架构介绍
        核心:api+case+data
         |--ipa:请求业务(requests)
         |--Caes:测试用例(unittest)
         |--data:参数化(json文件封装数据)
"""
#
import os

import logging
import logging.handlers

# 封装 URL 的前缀
import time
from fileinput import filename

BASE_URL = "http://182.92.81.159/api/sys/"
# 动态获取绝对路径
PRO_PATH = os.path.dirname(os.path.abspath(__file__))

def my_log_config():
    # 2.
    # 获取日志器对象
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # 3.
    # 设置日志处理器
    to1 = logging.StreamHandler()
    filename= PRO_PATH + "/log/myAuto" + time.strftime("%Y%m%d%H%M%S") + ".log"
    to2 = logging.handlers.TimedRotatingFileHandler(filename=filename,when="h",interval=10,backupCount=20,encoding="utf-8")
    # 4.
    # 设置格式化器
    fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d)] -%(message)s"
    formatter = logging.Formatter(fmt)
    # 5.
    # 组织上述对象
    to1.setFormatter(formatter)
    to2.setFormatter(formatter)
    logger.addHandler(to1)
    logger.addHandler(to2)



# 封装 URL 的前缀
BASE_URL = "http://182.92.81.159/api/sys/"
# 动态获取
PRO_PATH = os.path.dirname(os.path.abspath(__file__))
TOKEN = None
