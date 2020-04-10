# -*- coding: utf-8 -*-
# Time ： 2020/4/10 22:12
# Auth ： beibei
from test_appium.page.App import App


class TestProfile:
    def setup(self):
        self.profile = App().start().main().goto_profile()

    def test_login_by_password(self):
        assert  "错误" in self.profile.login_by_password("15667676767","123456")
