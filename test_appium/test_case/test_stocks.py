# -*- coding: utf-8 -*-
# Time ： 2020/4/11 14:04
# Auth ： beibei
from test_appium.page.App import App


class TestStocks:
    def setup(self):
        self.main = App().start().main()

    def test_stocks_select(self):
        """进入行情页，搜索股票并添加自选，然后重新回到行情页，验证京东是否在"""
        assert '京东' in self.main.goto_stocks().stocks_search('jd').stocks_select().stocks_get_msg()

