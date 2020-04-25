# -*- coding: utf-8 -*-
# Time ： 2020/4/19 21:56
# Auth ： beibei
from test_requests.test_wework.api.wework import WeWork


class ExternalContact(WeWork):
    def list(self):
        """获取客户列表"""
        pass

    def get(self):
        """获取客户详情"""
        pass

    def remark(self):
        """修改客户备注信息"""
        pass