# -*- coding: utf-8 -*-
# Time ： 2020/4/10 0:18
# Auth ： beibei
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from test_appium.page.base_page import BasePage
from test_appium.page.profile import Profile
from test_appium.page.search import Search


class Main(BasePage):

    def goto_search_page(self):
        self.find_element(MobileBy.ID, "tv_search").click()
        return Search(self._driver)

    def goto_stocks(self):
        pass

    def goto_trade(self):
        pass


    def goto_profile(self):
        self.find_element(By.XPATH, "//*[@text='我的']").click()
        return Profile(self._driver)

    def goto_message(self):
        pass