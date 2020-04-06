# -*- coding: utf-8 -*-
'''
@Time ： 2020/3/28 22:11
@Auth ： beibei
@File ：test_main.py
'''
from test_selenium.page.main import Main


class TestMain:
    def setup(self):
        self.main=Main(reuse=True)
    def test_add_member(self):
        self.main.goto_add_member().add_member("aaa")
        assert "aaa" in self.main.import_user().get_message()

    def test_import_user(self):
        self.main.import_user("D://test/pycharm/script/test_selenium/通讯录批量导入模板.xlsx")
        #assert  "success" in self.main.get_message()

    def test_add_image(self):
        self.main.goto_manageTools().add_image("D://test/pycharm/script/test_selenium/1.png")


    def test_send_message(self):
        message= self.main.send_message()
        message.send(app="十一",content="content",group="十一",member="王贝贝")
        #assert "content" in message.get_history()
        #  pass