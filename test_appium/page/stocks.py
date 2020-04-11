# -*- coding: utf-8 -*-
# Time ： 2020/4/11 13:44
# Auth ： beibei
import time

from selenium.webdriver.common.by import By

from test_appium.page.base_page import BasePage


class Stocks(BasePage):
    def stocks_search(self, key):
        """行情里搜索key"""
        # 点击行情页的选择放大镜，隐式等待
        self.find_element(By.ID, 'action_search').click()
        time.sleep(2)

        #输入搜索关键字，并选择第一个搜索到的内容
        self.find_element(By.ID, 'search_input_text').send_keys(key)
        time.sleep(1)
        self.find_element(By.ID, 'name').click()
        return self

    def stocks_select(self):
        """行情加自选"""
        # 添加自选
        self.find_element(By.XPATH, "//*[@text='加自选']").click()
        # todo : 是否需要加时间等待，不确定

        # 点击取消
        self.find_element(By.ID, 'action_close').click()
        return self

    def stocks_get_msg(self):
        """获取行情页的关键字"""
        return self.find_and_get_text(By.ID, 'portfolio_stockName')





