import pymysql.cursors
from model.entry import Entry
from model.group import Group


class DbFixture:
    def __init__(self, host, name, user, password, port):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.port = port
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, port=port, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

    def get_entry_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, middlename, lastname, nickname, title, company, address, home, mobile,"
                           " work, email, email2, email3, homepage, bday, bmonth, byear, aday, amonth, ayear from addressbook"
                           " where deprecated is null")
            for row in cursor:
                (id, firstname, middlename, lastname, nickname, title, company, address, home, mobile, work, email, email2, email3, homepage, bday, bmonth, byear, aday, amonth, ayear) = row
                list.append(Entry(id=str(id), firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname,
                                       title=title, company=company, address=address,
                                       phone_home=home, phone_mobile=mobile, phone_work=work,
                                       email=email, email2=email2, email3=email3,
                                       homepage_url=homepage,
                                       birth_day=str(bday), birth_month=bmonth, birth_year=byear,
                                       anniversary_day=str(aday), anniversary_month=amonth, anniversary_year=ayear))
        finally:
            cursor.close()
        return list