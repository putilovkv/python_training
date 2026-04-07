from test.helper import *
from model.entry import Entry
from model.group import Group


def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    db_list = make_groups_like_on_groups_page(db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)

def test_entry_list(app, db):
    ui_list = app.entry.get_entry_list()
    db_list = make_entries_like_on_homepage(db.get_entry_list())
    assert sorted(ui_list, key=Entry.id_or_max) == sorted(db_list, key=Entry.id_or_max)