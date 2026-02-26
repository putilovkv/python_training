# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from test_base import TestBase
from entry import Entry


class TestAddEntry(TestBase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_entry(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.create_entry(wd, Entry(firstname="Иван", middlename="Иванович", lastname="Иванов", nickname="косой",
                                    title="заголовок", company="самая лучшая компания", address="адрес компании",
                                    phone_home="73831234567", phone_mobile="79139130001", phone_work="73831122334",
                                    email="email1@google.com", email2="email2@google.com", email3="email3@google.com",
                                    homepage_url="home page url",
                                    birth_day="27", birth_month="December", birth_year="1988",
                                    anniversary_day="28", anniversary_month="November", anniversary_year="2000"))
        self.return_to_home_page(wd)
        self.logout(wd)

if __name__ == "__main__":
    unittest.main()
