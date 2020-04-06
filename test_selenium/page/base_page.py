# -*- coding: utf-8 -*-
'''
@Time ： 2020/3/28 23:33
@Auth ： beibei
@File ：base_page.py
'''
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = ""

    # _driver=None
    def __init__(self, driver: WebDriver = None, reuse=False):
        if driver is None:
            if reuse:
                chromeOptions = Options()
                chromeOptions.debugger_address = "127.0.0.1:9222"
                # 使用已经存在的chrome进程,chrome --remote-debugging-port=9222,查看是否有9222进程：netstat -p tcp -an
                self._driver = webdriver.Chrome(options=chromeOptions)
            else:
                # index页面的使用这个
                self._driver = webdriver.Chrome()
                # self._driver.get(self._base_url)
        else:
            # Login与Register等页面需要用这个方法
            self._driver = driver

        if self._base_url != "":
            self._driver.get((self._base_url))
        self._driver.implicitly_wait(3)

    def find(self, by, locator):
        if isinstance(by, tuple):
            return self._driver.find_element(*by)
        else:
            return self._driver.find_element(by, locator)

    # def find(self, locator):# locator是个元组
    #     return self._driver.find_element(*locator)

    def close(self):
        time.sleep(20)
        self._driver.quit()
