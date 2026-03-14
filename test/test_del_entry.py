# -*- coding: utf-8 -*-
from random import randrange
from model.entry import Entry


def test_delete_some_entry(app):
    if app.entry.count() == 0:
        app.entry.create(Entry(firstname="test_delete_first_entry"))
    old_entries = app.entry.get_entry_list()
    index = randrange(len(old_entries))
    app.entry.delete_entry_by_index(index)
    assert len(old_entries) - 1 == app.entry.count()
    new_entries = app.entry.get_entry_list()
    old_entries[index:index+1] = []
    assert old_entries == new_entries