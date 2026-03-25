# -*- coding: utf-8 -*-
import pytest
import random
import calendar
from model.entry import Entry
from test.helper import random_string


testdata = ([Entry(firstname=random_string("fn", 30),
                   middlename=random_string("mn", 30),
                   lastname=random_string("ln", 30),
                   nickname=random_string("nn", 30),
                   title=random_string("ti", 30),
                   company=random_string("co", 30),
                   address=random_string("nn", 30, use_newline=True),
                   phone_home=random_string("ph", 20),
                   phone_mobile=random_string("pm", 20),
                   phone_work=random_string("pw", 20),
                   email=random_string("e1", 30),
                   email2=random_string("e2", 30),
                   email3=random_string("e3", 30),
                   homepage_url=random_string("ur", 50),
                   birth_day=random.choice([str(x) for x in range(1, 32)] + ["-"]),
                   birth_month=random.choice(list(calendar.month_name)[1:] + ["-"]),
                   birth_year=random_string("", 4),
                   anniversary_day=random.choice([str(x) for x in range(1, 32)] + ["-"]),
                   anniversary_month=random.choice(list(calendar.month_name)[1:] + ["-"]),
                   anniversary_year=random_string("", 4))
             for i in range(5)])

@pytest.mark.parametrize("entry", testdata, ids=[repr(x) for x in testdata])
def test_add_entry(app, entry):
    old_entries = app.entry.get_entry_list()
    app.entry.create(entry)
    assert len(old_entries) + 1 == app.entry.count()
    new_entries = app.entry.get_entry_list()
    old_entries.append(entry)
    assert sorted(old_entries, key=Entry.id_or_max) == sorted(new_entries, key=Entry.id_or_max)