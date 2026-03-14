from fixture.base_helper import BaseHelper
from model.group import Group


class GroupHelper(BaseHelper):

    def __init__(self, app):
        super().__init__(app)
        self.__group_cache = None

    def create(self, group: Group):
        wd = self.app.wd
        self.app.navigation.go_to_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self._fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.__group_cache = None
        self.app.navigation.go_to_groups_page()

    def modify_first_group(self, new_group_data: Group):
        wd = self.app.wd
        self.app.navigation.go_to_groups_page()
        self._select_first_group()
        # open modification form
        wd.find_element_by_name("edit").click()
        self._fill_group_form(new_group_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.__group_cache = None
        self.app.navigation.go_to_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.app.navigation.go_to_groups_page()
        self._select_first_group()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.__group_cache = None
        self.app.navigation.go_to_groups_page()

    def count(self):
        wd = self.app.wd
        self.app.navigation.go_to_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_group_list(self):
        if self.__group_cache is None:
            wd = self.app.wd
            self.app.navigation.go_to_groups_page()
            self.__group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                name = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.__group_cache.append(Group(name=name, id=id))
        return list(self.__group_cache)

    def _select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def _fill_group_form(self, group: Group):
        self._change_field("group_name", group.name)
        self._change_field("group_header", group.header)
        self._change_field("group_footer", group.footer)