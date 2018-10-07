# -*- coding: utf-8 -*-
from appium import webdriver
capabilities = {
  "platformName": "Android",
  "deviceName": "127.0.0.1:62001",
  "app": "D:\\mukewang.apk"
}
webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
