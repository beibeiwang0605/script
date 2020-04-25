# -*- coding: utf-8 -*-
# Time ： 2020/4/19 21:03
# Auth ： beibei
import json

import requests
import yaml

from test_requests.test_wework.api.wework import WeWork


class User(WeWork):
    secret = 'GENL5nktkraesV2hgMtGFxlbIJDTErtAt8SJWCO4qYw'

    def __int__(self):
        self.data=self.api_load('../user/user_api.yaml')
        print(self.data)

    def create(self, userid, name, mobile):
        url='https://qyapi.weixin.qq.com/cgi-bin/user/create'
        r = requests.post(
                    url,
                    params={"access_token":self.get_token(self.secret),
                            'userid':userid,
                            'name':name,
                            'mobile':mobile}
        )
        print(json.dumps(r.json(), indent=2))
        return r.json()

    def get(self, userid):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/get'
        r = requests.get(
            url,
            params={"access_token": self.get_token(self.secret),
                    'userid': userid}
        )
        print(json.dumps(r.json(), ensure_ascii=False, indent=3))
        return r.json()

    def get_steps(self, userid, **kwargs):
        self.params['userid']=userid
        return self.api_send(self.data)

    def update(self, userid):
        url="https://qyapi.weixin.qq.com/cgi-bin/user/update"
        r = requests.post(
            url,
            params={"access_token": self.get_token(self.secret),
                    'userid': userid}
        )
        print(json.dumps(r.json(), indent=2))
        return r.json()

    def delete(self):
        pass