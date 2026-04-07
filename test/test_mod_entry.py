# -*- coding: utf-8 -*-
import random
from test.helper import *
from model.entry import Entry


def test_modify_entry(app, db, json_entries, check_ui):
    if len(db.get_entry_list()) == 0:
        app.entry.create(Entry(firstname="test_modify_first_entry"))
    old_entries = db.get_entry_list()
    old_entry = random.choice(old_entries)
    entry = json_entries
    app.entry.modify_entry_by_id(old_entry.id, entry)
    entry.fill_if_none(old_entry)
    new_entries = db.get_entry_list()
    old_entries[old_entries.index(old_entry)] = entry
    assert sorted(old_entries, key=Entry.id_or_max) == sorted(new_entries, key=Entry.id_or_max)
    if check_ui:
        new_entries = make_entries_like_on_homepage(new_entries)
        assert sorted(new_entries, key=Entry.id_or_max) == sorted(app.entry.get_entry_list(), key=Entry.id_or_max)