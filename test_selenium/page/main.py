# -*- coding: utf-8 -*-
'''
@Time ： 2020/3/28 22:03
@Auth ： beibei
@File ：main.py
'''
from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage
from test_selenium.page.contact import Contact
from test_selenium.page.manageTools import ManageTools
from test_selenium.page.message import Message


class Main(BasePage):
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame'

    def download(self):
        pass

    def import_user(self, path):
        self.find(By.PARTIAL_LINK_TEXT, '导入通讯录').click()
        # 文件上传
        self.find(By.ID, 'js_upload_file_input').send_keys(path)
        self.find(By.ID, 'submit_csv').click()
        self.find(By.ID, 'reloadContact').click()
        return self

    def goto_manageTools(self):
        self.find(By.PARTIAL_LINK_TEXT, '管理工具').click()
        return ManageTools(self._driver)

    def goto_app(self):
        pass

    def goto_company(self):
        pass

    def get_message(self):
        return ["aaa", "bbb"]

    def goto_add_member(self):
        locator = (By.LINK_TEXT, '添加成员')
        # 当浏览器zoom缩小时，找不到元素，可以用下面的js点击
        self._driver.execute_script("arguments[0].click();", self.find(*locator))
        self.find(*locator).click()
        return Contact(self._driver)

    def send_message(self):
        self.find(By.PARTIAL_LINK_TEXT, '消息群发').click()
        return Message(self._driver)
