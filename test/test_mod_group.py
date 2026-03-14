# -*- coding: utf-8 -*-
from datetime import datetime
from model.group import Group


def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_modify_first_group"))
    old_groups = app.group.get_group_list()
    group = Group(name=f"new_grname_{datetime.now().strftime('%H:%M:%S.%f')}",
                  header=f"new grheader_{datetime.now().strftime('%H:%M:%S.%f')}",
                  footer=f"new grfooter_{datetime.now().strftime('%H:%M:%S.%f')}")
    group.fill_if_none(old_groups[0])
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_modify_group_name"))
    old_groups = app.group.get_group_list()
    group = Group(name=f"new_grname_{datetime.now().strftime('%H:%M:%S.%f')}")
    group.fill_if_none(old_groups[0])
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="test_modify_group_header"))
    old_groups = app.group.get_group_list()
    group = Group(header=f"new_grheader_{datetime.now().strftime('%H:%M:%S.%f')}")
    group.fill_if_none(old_groups[0])
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(footer="test_modify_group_footer"))
    old_groups = app.group.get_group_list()
    group = Group(footer=f"new_grfooter_{datetime.now().strftime('%H:%M:%S.%f')}")
    group.fill_if_none(old_groups[0])
    app.group.modify_first_group(Group(footer=f"new_grfooter_{datetime.now().strftime('%H:%M:%S.%f')}"))
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)