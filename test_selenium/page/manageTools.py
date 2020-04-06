# -*- coding: utf-8 -*-
'''
@Time ： 2020/3/31 21:04
@Auth ： beibei
@File ：manageTools.py
'''
from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage


class ManageTools(BasePage):
    def add_image(self,path):
        self.find(By.PARTIAL_LINK_TEXT,'素材库').click()
        self.find(By.CSS_SELECTOR,'.qui_tabNav > li:nth-child(3) > a').click()
        self.find(By.PARTIAL_LINK_TEXT,'添加图片').click()
        self.find(By.ID,'js_upload_input').send_keys(path)
        self.find(By.PARTIAL_LINK_TEXT,'完成').click()

