# -*- coding: utf-8 -*-
import random
from test.helper import *
from model.group import Group


def test_modify_group(app, db, json_groups, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test_modify_first_group"))
    old_groups = db.get_group_list()
    old_group = random.choice(old_groups)
    group = json_groups
    app.group.modify_group_by_id(old_group.id, group)
    group.fill_if_none(old_group)
    new_groups = db.get_group_list()
    old_groups[old_groups.index(old_group)] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        new_groups = make_groups_like_on_groups_page(new_groups)
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)