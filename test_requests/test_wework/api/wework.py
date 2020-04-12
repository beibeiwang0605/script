# -*- coding: utf-8 -*-
# Time ： 2020/4/12 21:55
# Auth ： beibei

import json
from datetime import datetime

import requests

from test_requests.test_wework.api.base_api import BaseApi


class WeWork(BaseApi):
    token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    token=dict()
    token_time=dict()
    corpid = "wwacbedeb1e6c0841d"
    secret = "gX8dx95r27l4lYqHahmdEsClEe2yeXNsZSkkoM-lX1c"

    @classmethod
    def get_token(cls, secret=secret):
        # todo : token制度发生变化，在这个地方决定是否重新获取
        # 避免重复请求，提高效率
        # todo:重构这里
        # if secret is None:
        #     return cls.token[secret]
        if secret not in cls.token.keys():
            r = cls.get_access_token(secret)
            # json格式化打印
            # print(json.dumps(r, indent=3))
            cls.token[secret] = r["access_token"]
            cls.token_time[secret]=datetime.now()
        return cls.token[secret]

    @classmethod
    def get_access_token(cls, secret= secret):
        r = requests.get(cls.token_url,
                         params={"corpid": cls.corpid, "corpsecret": secret}
                         )
        assert r.json()['errcode'] == 0
        # json格式化打印
        # print(json.dumps(r.json(), indent=3))
        cls.format(r)
        return r.json()




