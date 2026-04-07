# -*- coding: utf-8 -*-
from test.helper import *
from model.entry import Entry


def test_add_entry(app, db, json_entries, check_ui):
    entry = json_entries
    old_entries = db.get_entry_list()
    app.entry.create(entry)
    new_entries = db.get_entry_list()
    old_entries.append(entry)
    assert sorted(old_entries, key=Entry.id_or_max) == sorted(new_entries, key=Entry.id_or_max)
    if check_ui:
        new_entries = make_entries_like_on_homepage(new_entries)
        assert sorted(new_entries, key=Entry.id_or_max) == sorted(app.entry.get_entry_list(), key=Entry.id_or_max)