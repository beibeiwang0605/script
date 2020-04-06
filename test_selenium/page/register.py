# -*- coding: utf-8 -*-
'''
@Time ： 2020/3/28 23:12
@Auth ： beibei
@File ：register.py
'''
from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage


class Register(BasePage):

    def register(self, corpname):
        self.find(By.ID, 'corp_name').click()
        self.find(By.ID, 'corp_name').send_keys(corpname)
        self.find(By.ID, 'submit_btn').click()
        return self

    def get_error_message(self):
        result = []
        for element in self.find(By.CSS_SELECTOR, '.js_error_msg'):
            result.append(element.text)
        return result
