# -*- coding: utf-8 -*-
# Time ： 2020/4/15 20:42
# Auth ： beibei
import requests

from test_requests.test_wework.api.wework import WeWork


class Department(WeWork):
    secret ="GENL5nktkraesV2hgMtGFxlbIJDTErtAt8SJWCO4qYw"

    def create(self, name, parentid, **kwargs):
        """创建部门"""
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        payload = {"name": name, "parentid": parentid}
        payload.update(kwargs)
        r = requests.post(
            url,
            params={"access_token": self.get_token(self.secret)},
            json=payload)
        self.format(r)
        return r.json()

    def update(self, id, **kwargs):
        """修改部门"""
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/update"
        payload = {"id": id}
        payload.update(kwargs)
        r = requests.post(
            url,
            params={"access_token": self.get_token(self.secret)},
            json=payload)
        self.format(r)
        return r.json()

    def delete(self, id):
        """删除部门"""
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/delete"
        r = requests.get(
            url,
            params={"access_token": self.get_token(self.secret),
                    "id": id}
            )
        self.format(r)
        return r.json()

    def list(self, id):
        """查询列表"""
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/list"
        r = requests.get(url,
                          params={"access_token": self.get_token(self.secret),
                                 "id": id}
                         )
        self.format(r)
        return r.json()