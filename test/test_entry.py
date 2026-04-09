# -*- coding: utf-8 -*-
from test.helper import *
from random import randrange
from model.entry import Entry

def test_some_entry_as_on_edit_page(app):
    all_entries = app.entry.get_entry_list()
    index = randrange(len(all_entries))
    entry_from_home_page = all_entries[index]
    entry_from_edit_page = app.entry.get_entry_info_from_edit_page(index)
    assert entry_from_home_page.lastname == remove_multiple_spaces_like_on_homepage(entry_from_edit_page.lastname)
    assert entry_from_home_page.firstname == remove_multiple_spaces_like_on_homepage(entry_from_edit_page.firstname)
    assert entry_from_home_page.address == remove_multiple_spaces_like_on_homepage(entry_from_edit_page.address)
    assert entry_from_home_page.all_emails_from_home_page == merge_emails_like_on_homepage(entry_from_edit_page)
    assert entry_from_home_page.all_phones_from_home_page == merge_phones_like_on_homepage(entry_from_edit_page)

def test_entry_list_as_from_db(app, db):
    ui_list = app.entry.get_entry_list()
    db_list = make_entries_like_on_homepage(db.get_entry_list())
    assert sorted(ui_list, key=Entry.id_or_max) == sorted(db_list, key=Entry.id_or_max)