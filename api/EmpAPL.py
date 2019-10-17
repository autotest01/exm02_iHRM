"""
    封装员工的增删改查请求实现
"""
import app



class EmpCRUD:
    # 函数:增
    def add(self, session, username, mobile,workNumber):

        myAddEmp = {
            "username": username,
            "mobile": mobile,
            "workNumber": workNumber}

        return session.post(app.BASE_URL + "user",
                            json=myAddEmp,
                            headers={"Authorization": "Bearer " + app.TOKEN})

        pass

    # 函数:改
    def update(self, session, userId, username):
        return session.put(app.BASE_URL + "user/" + userId,
                           json={"username": username},
                           headers={"Authorization": "Bearer " + app.TOKEN})



    # 函数:查
    def get(self,session,userId):
        return session.get(app.BASE_URL + "user/" +userId,
                           headers={"Authorization":"Bearer " + app.TOKEN})

    # 函数:删
    def delete(self,session,userId):
        return session.delete(app.BASE_URL + "user/" +userId,
                           headers={"Authorization":"Bearer " + app.TOKEN})
