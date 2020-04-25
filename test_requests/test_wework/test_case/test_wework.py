# -*- coding: utf-8 -*-
# Time ： 2020/4/12 20:03
# Auth ： beibei

import requests
from test_requests.test_wework.api.wework import WeWork
from test_requests.test_wework.api.groupchat import GroupChat


class TestWeWork:
    secret = "gX8dx95r27l4lYqHahmdEsClEe2yeXNsZSkkoM-lX1c"
    token = None

    @classmethod
    def setup_class(cls):
        """获取token，作为全局使用(类方法)"""
        # cls.token = WeWork.get_token()
        cls.token_steps=WeWork()

    def test_get_token(self):
        r = WeWork.get_access_token()
        assert r['errcode'] == 0
        # print(r.json())
        # json格式化打印
        # print(json.dumps(r.json(), indent=3))
        # self.token = r["access_token"]

    def test_get_token_exist(self):
        assert self.token is not None

    # 测试步骤驱动，获取token
    def test_get_token_steps(self):
        self.token_steps.get_token_steps()




