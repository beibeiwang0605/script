# -*- coding: utf-8 -*-
'''
@Time ： 2020/3/31 22:01
@Auth ： beibei
@File ：message.py
'''
import time

from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage


class Message(BasePage):
    def send(self,app="",content="",group="",member=""):
        self.find(By.LINK_TEXT,'选择需要发消息的应用').click()
        self.find(By.CSS_SELECTOR,'div[data-name*="%s"]' % group).click()
        #self.find(By.CSS_SELECTOR, 'div[data-name="测试开发十一期]').click()
        self.find(By.LINK_TEXT,'确定').click()

        self.find(By.LINK_TEXT,'选择发送范围').click()
        #todo 显示等待
        time.sleep(1)
        #self.find(By.ID,'memberSearchInput').click()
        # self._driver.find_elements(By.CSS_SELECTOR,'.ww_searchInput_text')[-1].click()   # 找到的元素里-1表示最后一个
        self.find(By.ID,'memberSearchInput').send_keys(member)
        self.find(By.CSS_SELECTOR,'#searchResult li').click()
        self.find(By.LINK_TEXT,'确认').click()

        self.find(By.CSS_SELECTOR,'textarea.js_send_msg_text').send_keys(content)
        time.sleep(2)
        #self.find(By.CSS_SELECTOR,'.msg_create .js_save_send:nth-child(1)').click()

        #self.find(By.LINK_TEXT,'发送').click()
        self.find(By.CSS_SELECTOR,'#js_createMessage78 >.msg_infoItem.msg_create_infoItem>.js_save_send').click()
        time.sleep(2)
        self.find(By.LINK_TEXT, '确定').click()
    def get_history(self):
        pass