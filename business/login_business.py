# -*- coding: utf-8 -*-
from handle.login_handle import LoginHandle

class LoginBusiness:

    def __init__(self,i):
        self.login_handle = LoginHandle(i)

    def login_pass(self):
        self.login_handle.send_username('13421382449')
        self.login_handle.send_pwd('123456')
        self.login_handle.click_login()

    def login_user_err(self):
        self.login_handle.send_username('1342cuowu')
        self.login_handle.send_pwd('123456')
        self.login_handle.click_login()
        flag = self.login_handle.get_fail_toast('账号未注册')
        if flag:
            return True
        else:
            return False

    def login_pwd_err(self):
        self.login_handle.send_username('1342cuowu')
        self.login_handle.send_pwd('123456aaa')
        self.login_handle.click_login()
        flag = self.login_handle.get_fail_toast('登录密码错误')
        if flag:
            return True
        else:
            return False