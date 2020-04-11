# -*- coding: utf-8 -*-
# Time ： 2020/4/10 0:24
# Auth ： beibei
import pytest
import yaml

from test_appium.page.App import App


class TestSearch:
    def setup(self):
        self.main = App().start().main()

    def test_search(self):
        assert self.main.goto_search_page().search("alibaba").get_price("baba") > 100

    # @pytest.mark.parametrize("key,stock_type,price",[
    #     ("alibaba","BABA",100),
    #     ("JD","JD",20)
    # ])
     # 数据驱动，使用yaml
    @pytest.mark.parametrize("key,stock_type,price", yaml.safe_load(open("data.yaml")))
    def test_search_data(self, key, stock_type, price):
        assert self.main.goto_search_page().search(key).get_price(stock_type) > price


    def test_select(self):
        assert '已添加' in self.main.goto_search_page().search('jd').add_select().get_msg()

    def test_unselect(self):
        self.main.goto_search_page().search('jd').un_select()

