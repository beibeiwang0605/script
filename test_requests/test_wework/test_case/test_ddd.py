# -*- coding: utf-8 -*-
# Time ： 2020/4/19 10:29
# Auth ： beibei
import pytest
import yaml
from jsonpath import jsonpath

from test_requests.test_wework.api.base_api import BaseApi
from test_requests.test_wework.api.tag import Tag


class TestDDD:
    # 单文件改为多文件
    #data=BaseApi.yaml_load("../test_case/test_tag.data.yaml")
    data=yaml.safe_load(open("../test_case/test_tag.all.yaml", encoding='utf-8'))
    #steps = yaml.safe_load(open("test_tag.step.yaml", encoding='utf-8'))
    #steps=BaseApi.yaml_load("test_tag.step.yaml")

    @classmethod
    def setup(cls):
        cls.tag=Tag()

    # @pytest.mark.parametrize("name",[
    #     "demo1","demo2","demo3","demo4","中文测试","中文"," ","*","✌",""
    # ])
    @pytest.mark.parametrize("name", data['data'])
    def test_delete(self, name):
        #name = "demo10"
        #如果有就删除
        r = self.tag.get()
        x = self.tag.jsonpath(r, f'$..tag[?(@.name=="{name}")]')
        if isinstance(x, list) and len(x) > 0:
            self.tag.delete(tag_id=[x[0]['id']])

        #环境干净后开始测试
        r = self.tag.get()
        path = "$..tag[?(@.name!='')]"
        # size= len(self.tag.jsonpath(r, '$..tag')[0])
        size = len(self.tag.jsonpath(r, path))

        # 添加新标签
        self.tag.add(name)
        r = self.tag.get()
        assert len(self.tag.jsonpath(r,path)) == size + 1

        #删除新标签
        tag_id=self.tag.jsonpath(r, f'$..tag[?(@.name=="{name}")]')[0]['id']
        self.tag.delete(tag_id=[tag_id])
        # 断言
        r = self.tag.get()
        assert len(self.tag.jsonpath(r, path)) == size

    @pytest.mark.parametrize("name", data['data'][0:1])
    def test_delete_steps(self, name):
        self.tag.params={"name":name}
        self.tag.steps_run(self.steps["steps"])



