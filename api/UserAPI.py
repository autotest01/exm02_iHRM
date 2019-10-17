"""
   封装登录请求
"""
import logging

import app


class Userlogin:

    # 登录请求
    def login(self,session,mobile,password):
        logging.info("log")
        myData={"mobile":mobile,"password":password}
        # return session对象.post("登录URL",json={"mobile":账号,"password":密码}
        return session.post(app.BASE_URL + "login",
                            json=myData)
