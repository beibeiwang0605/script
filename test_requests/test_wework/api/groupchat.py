# -*- coding: utf-8 -*-
# Time ： 2020/4/12 21:18
# Auth ： beibei
import json

import requests

from test_requests.test_wework.api.wework import WeWork


class GroupChat(WeWork):
    secret = "gX8dx95r27l4lYqHahmdEsClEe2yeXNsZSkkoM-lX1c"

    def list(self, offset=0,limit=1000, **kwargs):
        data={"offset": offset, "limit": limit}
        data.update(kwargs)
        print(kwargs)
        print(data)
        url = 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/list'
        r = requests.post(
            url,
            params={"access_token": self.get_token(self.secret)},
            json=data)
        # json格式化打印
        # todo : 自动加解密
        # todo: 多环境支持，根据配置可以一套case测试多套环境，需要修改host
        self.format(r)
        return r.json()

    def get(self,_chat_id):
        detail_url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/get"
        r = requests.post(
            detail_url,
            params={"access_token": self.get_token(self.secret)},
            json={"chat_id": _chat_id})
        self.format(r)
        return r.json()