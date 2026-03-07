# -*- coding: utf-8 -*-
from datetime import datetime
from model.entry import Entry


def test_modify_first_entry(app):
    app.session.login(username="admin", password="secret")
    app.entry.modify_first_entry(Entry(firstname=f"Петр_{datetime.now().strftime('%H:%M:%S.%f')}", middlename="Петрович", lastname="Петров", nickname="жулик",
                                title="новый заголовок", company="новая компания", address="новый адрес компании",
                                phone_home="73831112223", phone_mobile="79139137777", phone_work="73832223334",
                                email="new email1@google.com", email2="new email2@google.com", email3="new email3@google.com",
                                homepage_url="another home page url",
                                birth_day="2", birth_month="May", birth_year="1977",
                                anniversary_day="5", anniversary_month="July", anniversary_year="2020"))
    app.session.logout()

def test_modify_entry_firstname(app):
    app.session.login(username="admin", password="secret")
    app.entry.modify_first_entry(Entry(firstname=f"new_firstname_{datetime.now().strftime('%H:%M:%S.%f')}"))
    app.session.logout()

def test_modify_entry_middlename(app):
    app.session.login(username="admin", password="secret")
    app.entry.modify_first_entry(Entry(middlename=f"new_middlename_{datetime.now().strftime('%H:%M:%S.%f')}"))
    app.session.logout()

def test_modify_entry_lastname(app):
    app.session.login(username="admin", password="secret")
    app.entry.modify_first_entry(Entry(lastname=f"new_lastname_{datetime.now().strftime('%H:%M:%S.%f')}"))
    app.session.logout()