# -*- coding: utf-8 -*-
from test.helper import *
from model.group import Group


def test_group_list_as_from_db(app, db):
    ui_list = app.group.get_group_list()
    db_list = make_groups_like_on_groups_page(db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)