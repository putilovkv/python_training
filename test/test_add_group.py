# -*- coding: utf-8 -*-
from datetime import datetime
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name=f"grname_{datetime.now().strftime('%H:%M:%S.%f')}", header="grheader", footer="grfooter"))

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))