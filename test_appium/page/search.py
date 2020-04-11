# -*- coding: utf-8 -*-
# Time ： 2020/4/10 0:22
# Auth ： beibei
import time

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from test_appium.page.base_page import BasePage


class Search(BasePage):
    # 经常使用的控件或者定位可以放到这里维护
    #todo:多平台、多版本、多个可能定位符
    _name_locator = (MobileBy.ID, "name")
    def search(self, key: str):
        # self.find_element(MobileBy.ID, "search_input_text").send_keys(key)
        # #time.sleep(1)
        # self.find_element(self._name_locator).click()
        self._params={}
        self._params["key"]=key
        self.steps_yaml("../page/search.yaml")
        return self   # 支持链式调用
        # todo

    def get_price(self,key:str) -> float:
        return float(self._driver.find_element(MobileBy.ID, 'current_price').text)

    def add_select(self):
        element=self.find_by_text("加自选")
        element.click()
        return self

    def un_select(self):
        element = self.find_by_text("已添加")
        element.click()
        return self


    def get_msg(self):
        return self.find_and_get_text(By.ID, 'followed_btn')



