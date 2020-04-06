# -*- coding: utf-8 -*-
'''
@Time ： 2020/3/28 23:01
@Auth ： beibei
@File ：test_index.py
'''

from test_selenium.page.index import Index


class TestIndex:
    def setup(self):
        self.index = Index()

    def test_register(self):
        self.index.goto_register().register("测试学院")
        # self.driver.find_element(By.LINK_TEXT, '立即注册').click()
        # self.driver.find_element(By.ID, "corp_name").click()
        # self.driver.find_element(By.ID,"corp_name").send_keys("测试学院")
        # self.driver.find_element(By.ID,"submit_btn").click()

    def test_login(self):
        register_page = self.index.goto_login().goto_register().register("测试有限公司")
        print(register_page.get_error_message())
        print("|".join(register_page.get_error_message()))
        assert "请选择" in "|".join(register_page.get_error_message())

    def teardown(self):
        self.index.close()
