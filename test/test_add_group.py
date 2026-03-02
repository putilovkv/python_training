# -*- coding: utf-8 -*-
from datetime import datetime
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name=f"grname_{datetime.now().strftime('%H:%M:%S.%f')}", header="grheader", footer="grfooter"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

