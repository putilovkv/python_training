from sys import maxsize


class Entry:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None,
                 title=None, company=None, address=None,
                 phone_home=None, phone_mobile=None, phone_work=None,
                 email=None, email2=None, email3=None, homepage_url=None,
                 birth_day=None, birth_month=None, birth_year=None,
                 anniversary_day=None, anniversary_month=None, anniversary_year=None,
                 id=None, all_phones_from_home_page=None, all_emails_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.phone_home = phone_home
        self.phone_mobile = phone_mobile
        self.phone_work = phone_work
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage_url = homepage_url
        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.anniversary_day = anniversary_day
        self.anniversary_month = anniversary_month
        self.anniversary_year = anniversary_year
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return f"{self.id}:{self.lastname}, {self.firstname}, {self.address}, {self.all_emails_from_home_page}, {self.all_phones_from_home_page}"

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
                and self.lastname == other.lastname\
                and self.firstname == other.firstname\
                and (self.address or "") == (other.address or "")\
                and self.all_emails_from_home_page == other.all_emails_from_home_page\
                and self.all_phones_from_home_page == other.all_phones_from_home_page

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def fill_if_none(self, other):
        if self.firstname is None:
            self.firstname = other.firstname
        if self.middlename is None:
            self.middlename = other.middlename
        if self.lastname is None:
            self.lastname = other.lastname
        if self.nickname is None:
            self.nickname = other.nickname
        if self.title is None:
            self.title = other.title
        if self.company is None:
            self.company = other.company
        if self.address is None:
            self.address = other.address
        if self.phone_home is None:
            self.phone_home = other.phone_home
        if self.phone_mobile is None:
            self.phone_mobile = other.phone_mobile
        if self.phone_work is None:
            self.phone_work = other.phone_work
        if self.email is None:
            self.email = other.email
        if self.email2 is None:
            self.email2 = other.email2
        if self.email3 is None:
            self.email3 = other.email3
        if self.homepage_url is None:
            self.homepage_url = other.homepage_url
        if self.birth_day is None:
            self.birth_day = other.birth_day
        if self.birth_month is None:
            self.birth_month = other.birth_month
        if self.birth_year is None:
            self.birth_year = other.birth_year
        if self.anniversary_day is None:
            self.anniversary_day = other.anniversary_day
        if self.anniversary_month is None:
            self.anniversary_month = other.anniversary_month
        if self.anniversary_year is None:
            self.anniversary_year = other.anniversary_year
        if self.id is None:
            self.id = other.id
        if self.all_phones_from_home_page is None:
            self.all_phones_from_home_page = other.all_phones_from_home_page
        if self.all_emails_from_home_page is None:
            self.all_emails_from_home_page = other.all_emails_from_home_page
