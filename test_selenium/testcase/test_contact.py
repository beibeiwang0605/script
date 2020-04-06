# -*- coding: utf-8 -*-
'''
@Time ： 2020/3/28 21:56
@Auth ： beibei
@File ：test_contact.py
'''
from test_selenium.page.contact import Contact


class TestContact:
    def test_add_user(self):
        contact=Contact()
        Contact.add_member("xxx")
        Contact