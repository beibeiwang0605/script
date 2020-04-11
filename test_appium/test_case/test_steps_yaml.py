# -*- coding: utf-8 -*-
# Time ： 2020/4/11 16:37
# Auth ： beibei
from test_appium.page.App import App
from test_appium.page.base_page import BasePage

# 测试步骤page的数据驱动
class TestDD:
    def test_dd(self):
        """查看验证yaml文档数据的结构"""
        base=BasePage()
        base.yaml("D:/test/pycharm/script/test_appium/page/steps.yaml")

    def test_search_dd(self):
        App().start().main().goto_search_page().search('jd')

