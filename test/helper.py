import re
from model.group import Group
from model.entry import Entry


def make_groups_like_on_groups_page(groups):
    def clean(group):
        name = remove_multiple_spaces_like_on_homepage(group.name)
        return Group(id=group.id, name=name)
    return map(clean, groups)

def make_entries_like_on_homepage(entries):
    def clean(entry):
        firstname = remove_multiple_spaces_like_on_homepage(entry.firstname)
        lastname = remove_multiple_spaces_like_on_homepage(entry.lastname)
        address = remove_multiple_spaces_like_on_homepage(entry.address)
        all_phones = merge_phones_like_on_homepage(entry)
        all_emails = merge_emails_like_on_homepage(entry)
        return Entry(id=entry.id, firstname=firstname, lastname=lastname, address=address,
                     all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails)
    return map(clean, entries)

def merge_phones_like_on_homepage(entry):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: re.sub(r"[\u00A0\t.() -]", "", x),
                                filter(lambda x: x is not None,
                                       [entry.phone_home, entry.phone_mobile, entry.phone_work]))))

def merge_emails_like_on_homepage(entry):
    return "\n".join(filter(lambda x: x,
                            map (lambda x: remove_multiple_spaces_like_on_homepage(x),
                                 [entry.email, entry.email2, entry.email3])))

def remove_multiple_spaces_like_on_homepage(text):
    return "\n".join([re.sub(r"[\u00A0 ]+", " ", line).strip(" ") for line in text.splitlines()])