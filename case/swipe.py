# -*- coding: utf-8 -*-
from appium import webdriver
import time

def get_driver():
  capabilities = {
    "platformName": "Android",
    "deviceName": "127.0.0.1:62001",#3HX7N16C12000285
    "app": "D:\\mukewang_6220.apk",
    #"appWaitActivity":'cn.com.open.mooc.index.splash.GuideActivity',
    "noReset": True
  }
  driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
  return driver
#driver.swipe(700,400,50,400)
#driver.swipe(700,400,50,400,2000)

# 获得屏幕的宽高
def get_size(driver):
  size = driver.get_window_size()
  width = size['width']
  height = size['height']
  return width,height

# 向左滑动
def swipe_left(driver,duration):
  width, height = get_size(driver)
  x1 = width/10*9
  y1 = height/2
  x = width/10
  driver.swipe(x1,y1,x,y1,duration=duration)

# 向右滑动
def swipe_right(driver,duration):
  width, height = get_size(driver)
  x1 = width/10
  y1 = height/2
  x = width/10*9
  driver.swipe(x1,y1,x,y1,duration=duration)

# 向上滑动
def swipe_up(driver,duration):
  width, height = get_size(driver)
  x1 = width/2
  y1 = height/10*9
  y2 = height/10
  driver.swipe(x1,y1,x1,y2,duration=duration)

# 向下滑动
def swipe_down(driver,duration):
  width, height = get_size(driver)
  x1 = width/2
  y1 = height/10
  y2 = height/10*9
  driver.swipe(x1,y1,x1,y2,duration=duration)

# 滑动
def swipe_on(driver, direction,duration=None):
  if direction == 'left':
    swipe_left(driver,duration)
  elif direction == 'right':
    swipe_right(driver,duration)
  elif direction == 'up':
    swipe_up(driver,duration)
  else:
    swipe_down(driver,duration)

def loginIn(driver):
  driver.find_element_by_id('cn.com.open.mooc:id/tv_go_login').click()
  driver.find_element_by_id('cn.com.open.mooc:id/account_edit').send_keys('13421382449')
  driver.find_element_by_id('cn.com.open.mooc:id/password_edit').send_keys('84305684')
  driver.find_element_by_id('cn.com.open.mooc:id/login_lable').click()



#driver = get_driver()
#swipe_on(driver,'left')
#time.sleep(1)
#swipe_on(driver,'left')
#time.sleep(1)
#swipe_on(driver,'left')
#time.sleep(1)
#swipe_on(driver,'left')
#time.sleep(1)

#loginIn(driver)



