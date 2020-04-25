# -*- coding: utf-8 -*-
# Time ： 2020/4/19 21:12
# Auth ： beibei
import pytest

from test_requests.test_wework.api.base_api import BaseApi
from test_requests.test_wework.api.user.user import User


class TestUser:
    data = BaseApi.yaml_load('../test_case_user/test_user_data.yaml')

    def setup(self):
        self.user=User()


    def test_creat(self):
        r=self.user.create('wangxiabei123','王贝贝','18878788909')
        assert r["errcode"]==0

    """参数化"""
    @pytest.mark.parametrize('userid',['WangBeiBei',
                                     'wang_xiaoming',
                                     'wang_xiaoli'])
    def test_get_param(self, userid):
        r = self.user.get(userid)
        assert r['errcode']==0

    """参数化+ 测试数据驱动"""
    @pytest.mark.parametrize('userid',data['userid'])
    def test_get(self, userid):
        r = self.user.get(userid)
        assert r['errcode']==0

    @pytest.mark.parametrize('userid', data['userid'][0:1])
    def test_get_steps(self,userid):
        r = self.user.get_steps(userid)
        assert r['errcode']==0

    def test_update(self):
        r=self.user.update('wang_xiaoli')
        assert r['errcode'] == 0