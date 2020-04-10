# -*- coding: utf-8 -*-
# Time ： 2020/4/10 19:25
# Auth ： beibei
# 导入包的时候要导入对
from appium.webdriver.webdriver import WebDriver


class BasePage:
    _driver: WebDriver

    # 把app里的driver传递过来这里使用
    def __init__(self, driver:WebDriver = None):
        self._driver = driver

    #TODO:当有广告、评价等各种弹框出现的时候，要进行异常流程处理
    def find_element(self, by, locator:str = None):
        if isinstance(by, tuple):
            return self._driver.find_element(*by)
        else:
            return self._driver.find_element(by, locator)
