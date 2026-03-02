# -*- coding: utf-8 -*-
from datetime import datetime
from model.group import Group


def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name=f"new_grname_{datetime.now().strftime('%H:%M:%S.%f')}", header="new grheader", footer="new grfooter"))
    app.session.logout()