# -*- coding: utf-8 -*-
# Time ： 2020/4/10 0:22
# Auth ： beibei
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class Search:
    _driver: WebDriver

    # 把app里的driver传递过来这里使用
    def __init__(self, driver):
        self._driver = driver

    def search(self, key: str):
        self._driver.find_element(MobileBy.ID, "search_input_text").send_keys(key)
        self._driver.find_element(MobileBy.ID, "name").click()
        return self   # 支持链式调用
        # todo

    def get_price(self,key:str) -> float:
        return float(self._driver.find_element(MobileBy.ID, 'current_price').text)


