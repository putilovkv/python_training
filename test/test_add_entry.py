# -*- coding: utf-8 -*-
import pytest
from model.entry import Entry
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_entry(app):
    app.login(username="admin", password="secret")
    app.create_entry(Entry(firstname="Иван", middlename="Иванович", lastname="Иванов", nickname="косой",
                                title="заголовок", company="самая лучшая компания", address="адрес компании",
                                phone_home="73831234567", phone_mobile="79139130001", phone_work="73831122334",
                                email="email1@google.com", email2="email2@google.com", email3="email3@google.com",
                                homepage_url="home page url",
                                birth_day="27", birth_month="December", birth_year="1988",
                                anniversary_day="28", anniversary_month="November", anniversary_year="2000"))
    app.logout()
