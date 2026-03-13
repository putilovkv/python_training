# -*- coding: utf-8 -*-
from datetime import datetime
from model.entry import Entry


def test_add_entry(app):
    old_entries = app.entry.get_entry_list()
    entry = Entry(firstname=f"Иван_{datetime.now().strftime('%H:%M:%S.%f')}", middlename="Иванович", lastname="Иванов", nickname="косой",
                                title="заголовок", company="самая лучшая компания", address="адрес компании",
                                phone_home="73831234567", phone_mobile="79139130001", phone_work="73831122334",
                                email="email1@google.com", email2="email2@google.com", email3="email3@google.com",
                                homepage_url="home page url",
                                birth_day="27", birth_month="December", birth_year="1988",
                                anniversary_day="28", anniversary_month="November", anniversary_year="2000")
    app.entry.create(entry)
    new_entries = app.entry.get_entry_list()
    assert len(old_entries) + 1 == len(new_entries)
    old_entries.append(entry)
    assert sorted(old_entries, key=Entry.id_or_max) == sorted(new_entries, key=Entry.id_or_max)