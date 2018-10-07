# -*- coding: utf-8 -*-
from util.get_by_local import GetByLocal
from page.base_driver import BaseDriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BaseDriver):
    def __init__(self,i):
        self.driver = self.android_driver(i)
        self.gbl = GetByLocal(self.driver)
        self.page = 'LoginPage'


    def get_nameInput_ele(self):
        return self.gbl.get_element(self.page, 'nameInput')

    def get_pwdInput_ele(self):
        return self.gbl.get_element(self.page, 'pwdInput')

    def get_loginBtn_ele(self):
        return self.gbl.get_element(self.page, 'loginBtn')

    def get_toast_ele(self, msg):
        time.sleep(2)
        toast_ele = ("xpath","//*[contains(@text," + msg + ")]")
        return WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located(toast_ele))