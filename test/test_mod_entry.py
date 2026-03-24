# -*- coding: utf-8 -*-
from datetime import datetime
from random import randrange
from model.entry import Entry


def test_modify_entry_all(app):
    if app.entry.count() == 0:
        app.entry.create(Entry(firstname="test_modify_first_entry"))
    old_entries = app.entry.get_entry_list()
    index = randrange(len(old_entries))
    entry = Entry(firstname=f"Петр_{datetime.now().strftime('%H:%M:%S.%f')}",
                                       middlename=f"Петрович_{datetime.now().strftime('%H:%M:%S.%f')}",
                                       lastname=f"Петров_{datetime.now().strftime('%H:%M:%S.%f')}", nickname="жулик",
                                       title="новый заголовок", company="новая компания", address="новый адрес компании",
                                       phone_home="73831112223", phone_mobile="79139137777", phone_work="73832223334",
                                       email="new email1@google.com", email2="new email2@google.com", email3="new email3@google.com",
                                       homepage_url="another home page url",
                                       birth_day="2", birth_month="May", birth_year="1977",
                                       anniversary_day="5", anniversary_month="July", anniversary_year="2020")
    entry.fill_if_none(old_entries[index])
    app.entry.modify_entry_by_index(index, entry)
    assert len(old_entries) == app.entry.count()
    new_entries = app.entry.get_entry_list()
    old_entries[index] = entry
    assert sorted(old_entries, key=Entry.id_or_max) == sorted(new_entries, key=Entry.id_or_max)

def test_modify_entry_firstname(app):
    if app.entry.count() == 0:
        app.entry.create(Entry(firstname="test_modify_entry_firstname"))
    old_entries = app.entry.get_entry_list()
    index = randrange(len(old_entries))
    entry = Entry(firstname=f"new_firstname_{datetime.now().strftime('%H:%M:%S.%f')}")
    entry.fill_if_none(old_entries[index])
    app.entry.modify_entry_by_index(index, entry)
    assert len(old_entries) == app.entry.count()
    new_entries = app.entry.get_entry_list()
    old_entries[index] = entry
    assert sorted(old_entries, key=Entry.id_or_max) == sorted(new_entries, key=Entry.id_or_max)

def test_modify_entry_middlename(app):
    if app.entry.count() == 0:
        app.entry.create(Entry(middlename="test_modify_entry_middlename"))
    old_entries = app.entry.get_entry_list()
    index = randrange(len(old_entries))
    entry = Entry(middlename=f"new_middlename_{datetime.now().strftime('%H:%M:%S.%f')}")
    entry.fill_if_none(old_entries[index])
    app.entry.modify_entry_by_index(index, entry)
    assert len(old_entries) == app.entry.count()
    new_entries = app.entry.get_entry_list()
    old_entries[index] = entry
    assert sorted(old_entries, key=Entry.id_or_max) == sorted(new_entries, key=Entry.id_or_max)

def test_modify_entry_lastname(app):
    if app.entry.count() == 0:
        app.entry.create(Entry(lastname="test_modify_entry_lastname"))
    old_entries = app.entry.get_entry_list()
    index = randrange(len(old_entries))
    entry = Entry(lastname=f"new_lastname_{datetime.now().strftime('%H:%M:%S.%f')}")
    entry.fill_if_none(old_entries[index])
    app.entry.modify_entry_by_index(index, entry)
    assert len(old_entries) == app.entry.count()
    new_entries = app.entry.get_entry_list()
    old_entries[index] = entry
    assert sorted(old_entries, key=Entry.id_or_max) == sorted(new_entries, key=Entry.id_or_max)