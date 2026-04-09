# -*- coding: utf-8 -*-
import random
from test.helper import *
from model.entry import Entry


def test_add_entry_to_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test_add_entry_to_group"))
    group = random.choice(db.get_group_list())
    if len(db.get_entries_not_in_group(group)) == 0:
        app.entry.create(Entry(firstname=f"test_add_entry_to_group_{group.id}"))
    entry = random.choice(db.get_entries_not_in_group(group))
    app.entry.add_entry_to_group(entry.id, group.id)
    assert entry in db.get_entries_in_group(group)

def test_remove_entry_from_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test_remove_entry_from_group"))
    group = random.choice(db.get_group_list())
    if len(db.get_entries_in_group(group)) == 0:
        app.entry.create(Entry(firstname=f"test_remove_entry_from_group_{group.id}"), group.id)
    entry = random.choice(db.get_entries_in_group(group))
    app.entry.remove_entry_from_group(entry.id, group.id)
    assert entry not in db.get_entries_in_group(group)