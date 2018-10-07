# -*- coding: utf-8 -*-
from time import sleep
from appium import webdriver
from util.user_command import ReadUserCommand
class BaseDriver:
    def android_driver(self,i):
        #devicesName\port
        read_user_command = ReadUserCommand()
        deviceName = str(read_user_command.get_value('user_info_{}'.format(i),'deviceName'))
        port = str(read_user_command.get_value('user_info_{}'.format(i), 'port'))
        capabilities = {
            "platformName": "Android",
            "deviceName": deviceName,  # 3HX7N16C12000285     127.0.0.1:62001
            "app": "D:\\com.webank.wemoney.apk",
            "appPackage": "com.webank.wemoney",
            "appActivity": "com.webank.wemoney.EmptyActivity",
            "noReset": True
        }
        driver = webdriver.Remote("http://127.0.0.1:{}/wd/hub".format(port), capabilities)
        sleep(50)
        return driver

    def ios_driver(self):
        pass
