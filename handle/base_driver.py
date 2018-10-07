# -*- coding: utf-8 -*-
from time import sleep
from appium import webdriver
from util.user_command import ReadUserCommand
class BaseDriver:
    def android_driver(self, phone_num):
        read_user_command = ReadUserCommand()
        deviceName = str(
            read_user_command.get_value('user_info_{}'.format(phone_num), 'deviceName'))
        port = str(
            read_user_command.get_value('user_info_{}'.format(phone_num), 'port'))

        capabilities = {
            "platformName": "Android",
            "automationName": "uiautomator2",
            "deviceName": deviceName,  # 127.0.0.1:62001
            "app": "D:\\com.webank.wemoney.1809051630.apk",
            "appPackage": "com.webank.wemoney",
            "appActivity": "com.webank.wemoney.EmptyActivity",
            "noReset": True
        }
        driver = webdriver.Remote("http://127.0.0.1:{}/wd/hub".format(port), capabilities)
        driver.implicitly_wait(10)
        return driver

    def ios_driver(self):
        pass
