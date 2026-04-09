from fixture.base_helper import BaseHelper
from model.entry import Entry
from typing import List


class EntryHelper(BaseHelper):

    def __init__(self, app):
        super().__init__(app)
        self.__entry_cache = None

    def create(self, entry: Entry, group_id: str=None):
        wd = self.app.wd
        # init entry creation
        wd.find_element_by_link_text("add new").click()
        self._fill_entry_form(entry, group_id)
        # submit entry creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[19]").click()
        self.__entry_cache = None
        self.app.navigation.go_to_home_page()

    def modify_entry_by_index(self, index, new_entry_data: Entry):
        wd = self.app.wd
        self.app.navigation.go_to_home_page()
        self._open_entry_modification_form_by_index(index)
        self._fill_entry_form(new_entry_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.__entry_cache = None
        self.app.navigation.go_to_home_page()

    def modify_entry_by_id(self, index, new_entry_data: Entry):
        wd = self.app.wd
        self.app.navigation.go_to_home_page()
        self._open_entry_modification_form_by_id(index)
        self._fill_entry_form(new_entry_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.__entry_cache = None
        self.app.navigation.go_to_home_page()

    def modify_first_entry(self, new_entry_data: Entry):
        self.modify_entry_by_index(0, new_entry_data)

    def delete_entry_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.go_to_home_page()
        self._select_entry_by_index(index)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.__entry_cache = None
        self.app.navigation.go_to_home_page()

    def delete_entry_by_id(self, id):
        wd = self.app.wd
        self.app.navigation.go_to_home_page()
        self._select_entry_by_id(id)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.__entry_cache = None
        self.app.navigation.go_to_home_page()

    def delete_first_entry(self):
        self.delete_entry_by_index(0)

    def count(self) -> int:
        wd = self.app.wd
        self.app.navigation.go_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_entry_list(self) -> List[Entry]:
        if self.__entry_cache is None:
            wd = self.app.wd
            self.app.navigation.go_to_home_page()
            self.__entry_cache = []
            for element in wd.find_elements_by_name("entry"):
                tds = element.find_elements_by_tag_name("td")
                entry_id = tds[0].find_element_by_tag_name("input").get_attribute("id")
                lastname = tds[1].text
                firstname = tds[2].text
                address = tds[3].text
                all_emails = tds[4].text
                all_phones = tds[5].text
                self.__entry_cache.append(Entry(firstname=firstname, lastname=lastname, address=address, id=entry_id,
                                                all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails))
        return list(self.__entry_cache)

    def get_entry_info_from_edit_page(self, index) -> Entry:
        wd = self.app.wd
        self.app.navigation.go_to_home_page()
        self._open_entry_modification_form_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        middlename = wd.find_element_by_name("middlename").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        nickname = wd.find_element_by_name("nickname").get_attribute("value")
        title = wd.find_element_by_name("title").get_attribute("value")
        company = wd.find_element_by_name("company").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        phone_home = wd.find_element_by_name("home").get_attribute("value")
        phone_mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone_work = wd.find_element_by_name("work").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        homepage_url = wd.find_element_by_name("homepage").get_attribute("value")
        birth_day = wd.find_element_by_name("bday").get_attribute("value")
        birth_month = wd.find_element_by_name("bmonth").get_attribute("value")
        birth_year = wd.find_element_by_name("byear").get_attribute("value")
        anniversary_day = wd.find_element_by_name("aday").get_attribute("value")
        anniversary_month = wd.find_element_by_name("amonth").get_attribute("value")
        anniversary_year = wd.find_element_by_name("ayear").get_attribute("value")
        entry_id = wd.find_element_by_name("id").get_attribute("value")
        return Entry(firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname,
                     title=title, company=company, address=address,
                     phone_home=phone_home, phone_mobile=phone_mobile, phone_work=phone_work,
                     email=email, email2=email2, email3=email3, homepage_url=homepage_url,
                     birth_day=birth_day, birth_month=birth_month, birth_year=birth_year,
                     anniversary_day=anniversary_day, anniversary_month=anniversary_month, anniversary_year=anniversary_year,
                     id=entry_id)

    def add_entry_to_group(self, entry_id, group_id):
        wd = self.app.wd
        self.app.navigation.go_to_home_page()
        self._select_entry_by_id(entry_id)
        # select group to add entry to
        self._change_select_by_value("to_group", group_id)
        # submit addition
        wd.find_element_by_name("add").click()
        self.app.navigation.go_to_home_page()

    def remove_entry_from_group(self, entry_id, group_id):
        #Удалить контакт из группы (В выпадающем списке name="group" выбрать по id группу,выбрать контакт по id, в нажать кнопку name="remove")
        wd = self.app.wd
        self.app.navigation.go_to_home_page()
        # select group to remove entry from
        self._change_select_by_value("group", group_id)
        self._select_entry_by_id(entry_id)
        # submit removal
        wd.find_element_by_name("remove").click()
        self.app.navigation.go_to_home_page()

    def _select_entry_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def _select_entry_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector(f"input[id='{id}']").click()

    def _open_entry_modification_form_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def _open_entry_modification_form_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector(f"a[href='edit.php?id={id}']").click()

    def _select_first_entry(self):
        self._select_entry_by_index(0)

    def _fill_entry_form(self, entry: Entry, group_id: str=None):
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
        self._change_select_by_visible_text("bday", entry.birth_day)
        self._change_select_by_visible_text("bmonth", entry.birth_month)
        self._change_field("byear", entry.birth_year)
        self._change_select_by_visible_text("aday", entry.anniversary_day)
        self._change_select_by_visible_text("amonth", entry.anniversary_month)
        self._change_field("ayear", entry.anniversary_year)
        self._change_select_by_value("new_group", group_id)