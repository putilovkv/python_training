# -*- coding: utf-8 -*-
from datetime import datetime
from model.group import Group


def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_modify_first_group"))
    app.group.modify_first_group(Group(name=f"new_grname_{datetime.now().strftime('%H:%M:%S.%f')}",
                                       header=f"new grheader_{datetime.now().strftime('%H:%M:%S.%f')}",
                                       footer=f"new grfooter_{datetime.now().strftime('%H:%M:%S.%f')}"))

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_modify_group_name"))
    app.group.modify_first_group(Group(name=f"new_grname_{datetime.now().strftime('%H:%M:%S.%f')}"))

def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="test_modify_group_header"))
    app.group.modify_first_group(Group(header=f"new_grheader_{datetime.now().strftime('%H:%M:%S.%f')}"))

def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(footer="test_modify_group_footer"))
    app.group.modify_first_group(Group(footer=f"new_grfooter_{datetime.now().strftime('%H:%M:%S.%f')}"))