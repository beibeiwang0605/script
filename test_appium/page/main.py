# -*- coding: utf-8 -*-
# Time ： 2020/4/10 0:18
# Auth ： beibei
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from test_appium.page.base_page import BasePage
from test_appium.page.profile import Profile
from test_appium.page.search import Search
from test_appium.page.stocks import Stocks


class Main(BasePage):

    def goto_search_page(self):
        """进入搜索页"""
        # self.find_element(MobileBy.ID, "tv_search").click()
        self.steps_yaml("D:/test/pycharm/script/test_appium/page/steps.yaml")
        return Search(self._driver)

    def goto_stocks(self):
        """进入‘行情’页"""
        self.find_element(By.XPATH, '//*[@text="行情"]').click()
        return Stocks(self._driver)

    def goto_trade(self):
        """进入‘交易’页"""
        pass


    def goto_profile(self):
        """进入‘我的’"""
        self.find_element(By.XPATH, "//*[@text='我的']").click()
        return Profile(self._driver)

    def goto_message(self):
        pass