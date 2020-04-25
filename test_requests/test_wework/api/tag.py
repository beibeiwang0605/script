# -*- coding: utf-8 -*-
# Time ： 2020/4/19 10:24
# Auth ： beibei
import requests

from test_requests.test_wework.api.base_api import BaseApi
from test_requests.test_wework.api.wework import WeWork

# 装饰器
def api(fun):
    def magic(*args, **kwargs):
        base_api: BaseApi = args[0]
        method=fun.__name__
        base_api.params=kwargs
        req=base_api.api_load("../api/tag.api.yaml")[method]
        return base_api.api_send(req)
        #fun(*args, **kwargs)
    return magic

class Tag(WeWork):

    def __init__(self):
        secret = "gX8dx95r27l4lYqHahmdEsClEe2yeXNsZSkkoM-lX1c"
        self.params['access_token'] = self.get_token_steps(secret)
        self.data=self.api_load("../api/tag.api.yaml")

    def get(self):
        url="https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list"
        r=requests.post(url,
                        params={"access_token": self.get_token(self.secret)},
                        json={"tag_id":[]})
        self.format(r)
        return r.json()


    def add(self, name):
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag"
        r=requests.post(url,
                      params={"access_token": self.get_token(self.secret)},
                      json={"group_id":'etujavBgAAKhY7E1iwMSiIhNFz6WbRIg',
                            "tag":[
                          {
                              "name":name
                          }
                      ]
                      }
                    )
        self.format(r)
        return r.json()

    def update(self):
        pass

    def delete(self,tag_id=None, group_id=None):
        url="https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag"
        r = requests.post(url,
                          params={"access_token": self.get_token(self.secret)},
                          json={
                                "group_id": group_id,
                                "tag_id": [tag_id]
                                }
                          )
        self.format(r)
        return r.json()

    @api
    def xxx(self, age):
        pass

    # 测试步骤的驱动
    def get_api(self):
        return self.api_send(self.data['get'])

    # 测试步骤的驱动
    def add_api(self):
        # todo:用装饰器解决参数替换
        return self.api_send(self.data["add"])

    # 测试步骤的驱动
    def delete_api(self, tag_id=[], group_id=[]):
        # todo:用装饰器解决参数替换
        self.params["tag_id"] = tag_id
        self.params["group_id"] = group_id
        return self.api_send(self.data['delete'])