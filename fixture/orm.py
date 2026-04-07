from datetime import datetime
from pony.orm import *
from model.entry import Entry
from model.group import Group


class ORMFixture:
    db = Database()

    def __init__(self, host, name, user, password, port):
        self.db.bind('mysql', host=host, database=name, user=user, password=password, port=port, autocommit=True)
        self.db.generate_mapping()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        deprecated = Optional(datetime, column='deprecated')

    class ORMEntry(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        middlename = Optional(str, column='middlename')
        lastname = Optional(str, column='lastname')
        nickname = Optional(str, column='nickname')
        title = Optional(str, column='title')
        company = Optional(str, column='company')
        address = Optional(str, column='address')
        phone_home = Optional(str, column='home')
        phone_mobile =Optional(str, column='mobile')
        phone_work = Optional(str, column='work')
        email = Optional(str, column='email')
        email2 = Optional(str, column='email2')
        email3 = Optional(str, column='email3')
        homepage_url = Optional(str, column='homepage')
        birth_day = Optional(int, column='bday')
        birth_month = Optional(str, column='bmonth')
        birth_year = Optional(str, column='byear')
        anniversary_day = Optional(int, column='aday')
        anniversary_month = Optional(str, column='amonth')
        anniversary_year = Optional(str, column='ayear')
        deprecated = Optional(datetime, column='deprecated')

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.name)
        return list(map(convert, groups))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup if g.deprecated is None))

    def convert_entries_to_model(self, entries):
        def convert(entry):
            return Entry(id=str(entry.id),
                         firstname=entry.firstname,
                         middlename=entry.middlename,
                         lastname=entry.lastname,
                         nickname=entry.nickname,
                         title=entry.title,
                         company=entry.company,
                         address=entry.address,
                         phone_home=entry.phone_home,
                         phone_mobile=entry.phone_mobile,
                         phone_work=entry.phone_work,
                         email=entry.email,
                         email2=entry.email2,
                         email3=entry.email3,
                         homepage_url=entry.homepage_url,
                         birth_day=str(entry.birth_day),
                         birth_month=entry.birth_month,
                         birth_year=entry.birth_year,
                         anniversary_day=str(entry.anniversary_day),
                         anniversary_month=entry.anniversary_month,
                         anniversary_year=entry.anniversary_year)
        return list(map(convert, entries))

    @db_session
    def get_entry_list(self):
        return self.convert_entries_to_model(select(e for e in ORMFixture.ORMEntry if e.deprecated is None))