# -*- coding: utf-8 -*-
from appium import webdriver
from time import sleep
from swipe import *
capabilities = {
    "platformName": "Android",
    "automationName": "uiautomator2",
    "deviceName": "3HX7N16C12000285",#     127.0.0.1:62001
    "app": "D:\\com.webank.wemoney.1809051630.apk",
    "appPackage": "com.webank.wemoney",
    "appActivity": "com.webank.wemoney.EmptyActivity",
    "noReset": True
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
driver.implicitly_wait(10)
sleep(10)
print(driver.contexts)
# driver.find_element_by_android_uiautomator('new UiSelector().text("财富")').click()
# driver.find_element_by_android_uiautomator('new UiSelector().text("权益")').click()
# driver.find_element_by_android_uiautomator('new UiSelector().text("总览")').click()
# driver.find_element_by_android_uiautomator('new UiSelector().text("银行存款")').click()
# driver.find_elements_by_class_name('android.view.View')[0].click()
# sleep(2)
# driver.find_element_by_android_uiautomator('new UiSelector().text("近七日年化收益率")').click()
# # driver.find_elements_by_class_name('android.view.View')[0].click()
# # sleep(2)
# # driver.find_element_by_android_uiautomator('new UiSelector().text("短期+ 1~26天")').click()
# # driver.find_elements_by_class_name('android.view.View')[0].click()
# driver.find_element_by_xpath("//android.widget.TextView[@text='近七日年化收益率']").click()
# sleep(2)
# driver.find_element_by_xpath("//android.view.View").click()
# sleep(2)
# driver.find_element_by_xpath("//android.widget.TextView[@text='最高年利率']").click()
# sleep(2)
# driver.find_element_by_xpath("//android.view.View").click()
# sleep(2)
# driver.find_element_by_xpath("//android.widget.TextView[@text='短期+ 1~26天']").click()
# sleep(2)
# driver.find_element_by_xpath("//android.view.View").click()
# sleep(2)
# swipe_on(driver, 'up')
#
# driver.find_element_by_xpath("//android.widget.TextView[@text='专业人士打理']").click()
# sleep(2)
# driver.find_element_by_xpath("//android.widget.ImageView").click()
# sleep(2)
# driver.find_element_by_xpath("//android.widget.TextView[@text='生息实物黄金']").click()
# sleep(2)
# driver.find_element_by_xpath("//android.view.View").click()
#

driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup[1]/android.view.ViewGroup[4]/android.view.ViewGroup[1]").click()
sleep(2)
driver.find_element_by_xpath("//android.view.ViewGroup/android.view.View[1]").click()
sleep(2)
driver.find_element_by_xpath("//android.widget.TextView[@text='近七日年化收益率']").click()
sleep(2)
driver.find_element_by_xpath("//android.view.ViewGroup/android.view.ViewGroup[1]/android.view.View[1]").click()
sleep(2)
driver.find_element_by_xpath("//android.widget.TextView[@text='定期+ 30天以上']").click()
sleep(2)
driver.find_element_by_xpath("//android.view.ViewGroup/android.view.View[1]").click()
sleep(2)
swipe_on(driver, 'up')
driver.find_element_by_xpath("//android.widget.TextView[@text='专业人士打理']").click()
sleep(2)
driver.find_element_by_xpath("//android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ImageView[1]").click()
sleep(2)

driver.find_element_by_xpath("//android.widget.TextView[@text='生息实物黄金']").click()
sleep(2)
driver.find_element_by_xpath("//android.view.ViewGroup/android.view.View[1]").click()
sleep(2)