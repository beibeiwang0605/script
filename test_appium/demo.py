# -*- coding: utf-8 -*-
# Time ： 2020/4/4 12:14
# Auth ： beibei
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "hogwarts_11"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"
caps["automationName"] = "uiautomator2"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(20)

el1 = driver.find_element_by_id("com.xueqiu.android:id/tv_agree")
el1.click()
el2 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el2.click()
el3 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el3.send_keys("阿里巴巴")

driver.quit()

