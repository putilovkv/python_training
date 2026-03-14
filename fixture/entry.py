from fixture.base_helper import BaseHelper
from model.entry import Entry


class EntryHelper(BaseHelper):

    def __init__(self, app):
        super().__init__(app)
        self.__entry_cache = None

    def create(self, entry: Entry):
        wd = self.app.wd
        # init entry creation
        wd.find_element_by_link_text("add new").click()
        self._fill_entry_form(entry)
        # submit entry creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[19]").click()
        self.__entry_cache = None
        self.app.navigation.go_to_home_page()

    def modify_first_entry(self, entry: Entry):
        wd = self.app.wd
        self.app.navigation.go_to_home_page()
        self._select_first_entry()
        # open modification form
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self._fill_entry_form(entry)
        # submit modification
        wd.find_element_by_name("update").click()
        self.__entry_cache = None
        self.app.navigation.go_to_home_page()

    def delete_first_entry(self):
        wd = self.app.wd
        self.app.navigation.go_to_home_page()
        self._select_first_entry()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.__entry_cache = None
        self.app.navigation.go_to_home_page()

    def count(self):
        wd = self.app.wd
        self.app.navigation.go_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_entry_list(self):
        if self.__entry_cache is None:
            wd = self.app.wd
            self.app.navigation.go_to_home_page()
            self.__entry_cache = []
            for element in wd.find_elements_by_name("entry"):
                tds = element.find_elements_by_tag_name("td")
                id = tds[0].find_element_by_tag_name("input").get_attribute("id")
                lastname = tds[1].text
                firstname = tds[2].text
                self.__entry_cache.append(Entry(firstname=firstname, lastname=lastname, id=id))
        return list(self.__entry_cache)

    def _select_first_entry(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def _fill_entry_form(self, entry: Entry):
        wd = self.app.wd
        self._change_field("firstname", entry.firstname)
        self._change_field("middlename", entry.middlename)
        self._change_field("lastname", entry.lastname)
        self._change_field("nickname", entry.nickname)
        self._change_field("title", entry.title)
        self._change_field("company", entry.company)
        self._change_field("address", entry.address)
        self._change_field("home", entry.phone_home)
        self._change_field("mobile", entry.phone_mobile)
        self._change_field("work", entry.phone_work)
        self._change_field("email", entry.email)
        self._change_field("email2", entry.email2)
        self._change_field("email3", entry.email3)
        self._change_field("homepage", entry.homepage_url)
        self._change_select("bday", entry.birth_day)
        self._change_select("bmonth", entry.birth_month)
        self._change_field("byear", entry.birth_year)
        self._change_select("aday", entry.anniversary_day)
        self._change_select("amonth", entry.anniversary_month)
        self._change_field("ayear", entry.anniversary_year)