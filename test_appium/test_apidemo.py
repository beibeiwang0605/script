# -*- coding: utf-8 -*-
# Time ： 2020/4/4 12:14
# Auth ： beibei
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestApiDemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts_11"
        caps["appPackage"] = "io.appium.android.apis"
        caps["appActivity"] = ".ApiDemos"
        caps["automationName"] = "uiautomator2"
        # caps["noReset"] = True  # Ture表示不重置，False表示重置，数据被清理的过程
        # caps["dontStopAppOnReset"] = True
        # caps["unicodeKeyboard"]=True   # 是否需要输入非英文之外的语言，True表示"是“
        # caps["resetKeyBoard"] = True
        caps["skipServerInstallation"]=True   # 跳过系统安装，可以加速

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)
        # WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located())   # 显式等待

    def test_toast(self):
        """手机弹出的toast识别"""
        scroll_to_element = (MobileBy.ANDROID_UIAUTOMATOR,
                             'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                             '.scrollIntoView(new UiSelector().text("Views").instance(0));')
        self.driver.find_element(*scroll_to_element).click()

        scroll_to_element = (MobileBy.ANDROID_UIAUTOMATOR,
                             'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                             '.scrollIntoView(new UiSelector().text("Popup Menu").instance(0));')
        self.driver.find_element(*scroll_to_element).click()
        # self.driver.find_element(MobileBy.XPATH,'//*[@text="MAKE A POPUP!"]').click()
        # 可以使用MobileBy.ACCESSIBILITY_ID来定位content-desc
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID,'Make a Popup!').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="Search"]').click()
        toast= self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
        assert "Clicked popup menu item Search" in toast

    def teardown(self):
        time.sleep(10)
        self.driver.quit()






