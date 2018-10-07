# -*- coding: utf-8 -*-
from page.login_page import LoginPage

class LoginHandle():
    def __init__(self,i):
        self.login_page = LoginPage(i)

    def send_username(self, username):
        self.login_page.get_nameInput_ele().send_keys(username)

    def send_pwd(self, pwd):
        self.login_page.get_pwdInput_ele().send_keys(pwd)

    def click_login(self):
        self.login_page.get_loginBtn_ele().click()

    def get_fail_toast(self, msg):
        toast_ele = self.login_page.get_toast_ele(msg)
        if toast_ele:
            return True
        else:
            return False