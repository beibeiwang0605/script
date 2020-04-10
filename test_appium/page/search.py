# -*- coding: utf-8 -*-
# Time ： 2020/4/10 0:22
# Auth ： beibei
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from test_appium.page.base_page import BasePage


class Search(BasePage):
    # 经常使用的控件或者定位可以放到这里维护
    #todo:多平台、多版本、多个可能定位符
    _name_locator = (MobileBy.ID, "name")
    def search(self, key: str):
        self.find_element(MobileBy.ID, "search_input_text").send_keys(key)
        self.find_element(self._name_locator).click()
        return self   # 支持链式调用
        # todo

    def get_price(self,key:str) -> float:
        return float(self._driver.find_element(MobileBy.ID, 'current_price').text)


