# -*- coding: utf-8 -*-
'''
@Time ： 2020/3/28 23:44
@Auth ： beibei
@File ：login.py
'''
from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage
from test_selenium.page.register import Register


class Login(BasePage):
    def scan_qrcode(self):
        pass

    def goto_register(self):
        self.find(By.LINK_TEXT, '企业注册').click()
        return Register(self._driver)
