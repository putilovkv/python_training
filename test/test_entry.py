# -*- coding: utf-8 -*-
import re
from random import randrange

def test_entry_on_home_page(app):
    all_entries = app.entry.get_entry_list()
    index = randrange(len(all_entries))
    entry_from_home_page = all_entries[index]
    entry_from_edit_page = app.entry.get_entry_info_from_edit_page(index)
    assert entry_from_home_page.lastname == entry_from_edit_page.lastname
    assert entry_from_home_page.firstname == entry_from_edit_page.firstname
    assert entry_from_home_page.address == entry_from_edit_page.address
    assert entry_from_home_page.all_emails_from_home_page == merge_emails_like_on_homepage(entry_from_edit_page)
    assert entry_from_home_page.all_phones_from_home_page == merge_phones_like_on_homepage(entry_from_edit_page)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_homepage(entry):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [entry.phone_home, entry.phone_mobile, entry.phone_work]))))

def merge_emails_like_on_homepage(entry):
    return "\n".join(filter(lambda x: x, [entry.email, entry.email2, entry.email3]))