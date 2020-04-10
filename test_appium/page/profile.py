# -*- coding: utf-8 -*-
# Time ： 2020/4/10 22:09
# Auth ： beibei
from selenium.webdriver.common.by import By

from test_appium.page.base_page import BasePage


class Profile(BasePage):
    def login_by_password(self, phone, password):
        self.find_element(By.XPATH, "//*[@text='帐号密码登录']").click()
        self.find_element(By.ID, 'login_account').send_keys(phone)
        self.find_element(By.ID, 'login_password').send_keys(password)
        self.find_element(By.ID, 'button_next').click()
        msg = self.find_element(By.ID, 'md_content').text
        self.find_element(By.ID, 'md_buttonDefaultPositive').click()
        return msg