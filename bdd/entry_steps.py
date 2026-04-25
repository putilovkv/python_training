from model.entry import Entry
from pytest_bdd import given, when, then, parsers
from test.helper import make_entries_like_on_homepage
import random


@given('a entry list', target_fixture="entry_list")
def entry_list(db):
    return db.get_entry_list()

@given('a non-empty entry list', target_fixture="non_empty_entry_list")
def non_empty_entry_list(db, app):
    if len(db.get_entry_list()) == 0:
        app.entry.create(Entry(lastname='entry lastname'))
    return db.get_entry_list()

@given(parsers.parse('a entry with {firstname}, {lastname}, {address}, {phone_home} and {email}'), target_fixture="new_entry")
def new_entry(firstname, lastname, address, phone_home, email):
    return Entry(firstname=firstname, lastname=lastname, address=address, phone_home=phone_home, email=email)

@given('a random entry from the list', target_fixture="random_entry")
def random_entry(non_empty_entry_list):
    return random.choice(non_empty_entry_list)

@when('I add the entry to the list')
def add_new_entry(app, new_entry):
    app.entry.create(new_entry)

@when('I edit the entry in the list')
def edit_entry(app, random_entry, new_entry):
    app.entry.modify_entry_by_id(random_entry.id, new_entry)

@when('I delete the entry from the list')
def delete_entry(app, random_entry):
    app.entry.delete_entry_by_id(random_entry.id)

@then('the new entry list is equal to the old list with added entry')
def verify_new_entry_added(db, entry_list, new_entry, app, check_ui):
    old_entries = entry_list
    new_entries = db.get_entry_list()
    old_entries.append(new_entry)
    assert sorted(old_entries, key=Entry.id_or_max) == sorted(new_entries, key=Entry.id_or_max)
    if check_ui:
        new_entries = make_entries_like_on_homepage(new_entries)
        assert sorted(new_entries, key=Entry.id_or_max) == sorted(app.entry.get_entry_list(), key=Entry.id_or_max)

@then('the new entry list is equal to the old list with edited entry')
def verify_entry_edited(db, non_empty_entry_list, random_entry, new_entry, app, check_ui):
    old_entries = non_empty_entry_list
    new_entry.fill_if_none(random_entry)
    new_entries = db.get_entry_list()
    old_entries[old_entries.index(random_entry)] = new_entry
    assert sorted(old_entries, key=Entry.id_or_max) == sorted(new_entries, key=Entry.id_or_max)
    if check_ui:
        new_entries = make_entries_like_on_homepage(new_entries)
        assert sorted(new_entries, key=Entry.id_or_max) == sorted(app.entry.get_entry_list(), key=Entry.id_or_max)

@then('the new entry list is equal to the old list without deleted entry')
def verify_entry_deleted(db, non_empty_entry_list, random_entry, app, check_ui):
    old_entries = non_empty_entry_list
    new_entries = db.get_entry_list()
    old_entries.remove(random_entry)
    assert old_entries == new_entries
    if check_ui:
        new_entries = make_entries_like_on_homepage(new_entries)
        assert sorted(new_entries, key=Entry.id_or_max) == sorted(app.entry.get_entry_list(), key=Entry.id_or_max)