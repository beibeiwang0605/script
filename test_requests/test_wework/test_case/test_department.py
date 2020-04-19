# -*- coding: utf-8 -*-
# Time ： 2020/4/15 20:54
# Auth ： beibei
from test_requests.test_wework.api.department import Department


class TestDepartment:

    def setup(self):
        self.department = Department()

    def test_creat(self):
        r = self.department.create("广东研发中心", 1)
        assert r['errcode'] == 0

    def test_update(self):
        r=self.department.update(2)
        assert  r["errcode"]==0

    def test_delete(self):
        r=self.department.delete(4)
        assert r["errcode"]==0

    def test_list(self):
        r=self.department.list(3)
        assert r["errcode"]==0