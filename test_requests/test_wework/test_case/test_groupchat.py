# -*- coding: utf-8 -*-
# Time ： 2020/4/12 20:03
# Auth ： beibei

import requests
from test_requests.test_wework.api.wework import WeWork
from test_requests.test_wework.api.groupchat import GroupChat


class TestGroupchat:
    # secret ="svWk8sPWM6hliL0agxvn19KG7jQifNnAT-oMjdGrDVU"
   # secret = "gX8dx95r27l4lYqHahmdEsClEe2yeXNsZSkkoM-lX1c"
    token = None

    @classmethod
    def setup_class(cls):
        """获取token，作为全局使用(类方法)"""
        cls.groupchat=GroupChat()
        # cls.token = WeWork.get_token(cls.groupchat.secret)

    # def test_get_list(self):
    #     userid="WangBeiBei"
    #     r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/list',
    #                      params={"access_token":self.groupchat.get_token(self.groupchat.secret),"userid":userid})
    # 客户群管理

    def test_groupchat_list(self):
        """获取客户群列表"""
        r = self.groupchat.list()
        assert r['errcode']==0

    def test_group_get_status(self):
        r=self.groupchat.list(status_filter=1)

    def test_groupchat_detail(self):
        """获取客户群详情"""
        # 先从列表获取到chat_id
        r = self.groupchat.list(offset=0, limit=10)
        assert r['errcode'] == 0
        chat_id = r['group_chat_list'][0]['chat_id']
        #再使用chat_id获取详情信息
        r = self.groupchat.get(_chat_id= chat_id)
        assert r['errcode'] == 0
        assert len(r['group_chat']['member_list']) > 0

