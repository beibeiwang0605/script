# -*- coding: utf-8 -*-
# Time ： 2020/4/10 0:16
# Auth ： beibei
import datetime

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.page.base_page import BasePage
from test_appium.page.main import Main


class App(BasePage):
    # def __init__(self, driver: WebDriver = None):
    #     super()
    def start(self):
        _package = "com.xueqiu.android"
        _activity = ".view.WelcomeActivityAlias"
        if self._driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "Android 9.0"
            caps["appPackage"] = _package
            caps["appActivity"] = _activity
            caps["automationName"] = "uiautomator2"
            #caps["noReset"] = True  # Ture表示不重置，False表示重置，数据被清理的过程
            # caps["dontStopAppOnReset"] = True
            caps["unicodeKeyboard"] = True  # 是否需要输入非英文之外的语言，True表示"是“
            caps["resetKeyBoard"] = True
            caps['autoGrantPermissions'] = True  # 让appium自动授权app权限，如果noReset为True，则该条不生效。
            # caps["chromedriverExecutableDir"] = "D:/test/chromedriver"
            caps["chromedriverExecutable"] = "D:/test/chromedriver/chrome_43.0.2357.0/chromedriver_2.20.exe"  # 指定chromedriver
            caps["avd"] = 'Android_9.0'  # 可以指定模拟器启动并运行

            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self._driver.implicitly_wait(5)
        else:
            print(self._driver)
            # todo :kill app start app
            self._driver.start_activity(_package, _activity)

        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self) -> Main:
        #todo: wait main page
        def wait_load(_driver):
            print(datetime.datetime.now())
            source = self._driver.page_source
            if "我的" in source:
                return True
            if "同意" in source:
                return True
            if "image_cancel" in source:
                return True
            if "下次再说" in source:
                return True
            return False
        WebDriverWait(self._driver,30).until(wait_load)  # 这里wait_load不需要加（），因为调用的是这个方法，不是方法里的内容
        return Main(self._driver)