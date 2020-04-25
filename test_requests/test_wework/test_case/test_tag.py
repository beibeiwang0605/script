# -*- coding: utf-8 -*-
# Time ： 2020/4/19 10:29
# Auth ： beibei
import pytest
import yaml
from jsonpath import jsonpath

from test_requests.test_wework.api.base_api import BaseApi
from test_requests.test_wework.api.tag import Tag


class TestTag:
    #data=BaseApi.yaml_load("../test_case/test_tag.data.yaml")
    data=yaml.safe_load(open("../test_case/test_tag.data.yaml", encoding='utf-8'))
    steps = yaml.safe_load(open("test_tag.step.yaml", encoding='utf-8'))
    #steps=BaseApi.yaml_load("test_tag.step.yaml")
    # print(data)

    @classmethod
    def setup(cls):
        cls.tag=Tag()

    def test_get(self):
        r=self.tag.get()
        assert r['errcode']==0
        print(self.tag.jsonpath('$..tag[?(@.name=="demo5")]')[0]['id'])

    def test_add(self):
        # 如果有就删除
        name = 'demo2'
        r = self.tag.get()
        x = self.tag.jsonpath(f'$..tag[?(@.name=="{name}")]')
        if isinstance(x, list) and len(x) > 0:
            self.tag.delete(tag_id=[x[0]['id']])
        # 删除后再新增
        r=self.tag.add(name)
        assert r["errcode"]==0

    # 使用测试步骤驱动的测试用例
    def test_get_api(self):
        r = self.tag.get_api()
        result=self.tag.jsonpath('$..tag[?(@.name=="fffff")]')
        print(result[0]['id'])
        assert r['errcode'] == 0

    # 使用测试步骤驱动的测试用例
    def test_add_api(self):
        # 如果有就删除
        name2 = 'fffff'
        r = self.tag.get()
        x = self.tag.jsonpath(f'$..tag[?(@.name=="{name2}")]')
        if isinstance(x, list) and len(x) > 0:
            self.tag.delete(tag_id=[x[0]['id']])
        # 删除后再新增
        self.tag.params["name"] = name2
        r = self.tag.add_api()
        assert r["errcode"] == 0

    # 使用测试步骤驱动的测试用例
    def test_delete_api(self):
        r = self.tag.get_api()
        result = self.tag.jsonpath('$..tag[?(@.name=="fffff")]')
        print(result[0]['id'])
        r = self.tag.delete_api(result[0]['id'])
        assert r["errcode"] == 0


    # @pytest.mark.parametrize("name",[
    #     "demo1","demo2","demo3","demo4","中文测试","中文"," ","*","✌",""
    # ])
    # 参数化驱动、yanl测试数据驱动
    @pytest.mark.parametrize("name", data['test_delete'])
    def test_delete(self, name):
        #如果有就删除
        r = self.tag.get()
        x = self.tag.jsonpath(f'$..tag[?(@.name=="{name}")]')
        if isinstance(x, list) and len(x) > 0:
            self.tag.delete(tag_id=[x[0]['id']])

        #环境干净后开始测试
        r = self.tag.get()
        path = "$..tag[?(@.name!='')]"
        # size= len(self.tag.jsonpath(r, '$..tag')[0])
        size = len(self.tag.jsonpath(path))

        # 添加新标签
        self.tag.add(name)
        r = self.tag.get()
        assert len(self.tag.jsonpath(path)) == size + 1

        #删除新标签
        tag_id=self.tag.jsonpath(f'$..tag[?(@.name=="{name}")]')[0]['id']
        self.tag.delete(tag_id=[tag_id])
        # 断言
        r = self.tag.get()
        assert len(self.tag.jsonpath(path)) == size

    # todo : 参数替换有问题
    @pytest.mark.parametrize("name", data['test_delete'][0:1])
    def test_delete_steps(self, name):
        self.tag.params={"name":name}
        self.tag.steps_run(self.steps["test_delete"])


    def test_xxx(self):
        self.tag.xxx()


