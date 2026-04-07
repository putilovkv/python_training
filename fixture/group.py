from fixture.base_helper import BaseHelper
from model.group import Group
from typing import List


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

    def modify_group_by_index(self, index, new_group_data: Group):
        wd = self.app.wd
        self.app.navigation.go_to_groups_page()
        self._select_group_by_index(index)
        # open modification form
        wd.find_element_by_name("edit").click()
        self._fill_group_form(new_group_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.__group_cache = None
        self.app.navigation.go_to_groups_page()

    def modify_first_group(self, new_group_data: Group):
        self.modify_group_by_index(0, new_group_data)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.go_to_groups_page()
        self._select_group_by_index(index)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.__group_cache = None
        self.app.navigation.go_to_groups_page()

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.app.navigation.go_to_groups_page()
        self._select_group_by_id(id)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.__group_cache = None
        self.app.navigation.go_to_groups_page()

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def count(self) -> int:
        wd = self.app.wd
        self.app.navigation.go_to_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_group_list(self) -> List[Group]:
        if self.__group_cache is None:
            wd = self.app.wd
            self.app.navigation.go_to_groups_page()
            self.__group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                name = element.text
                group_id = element.find_element_by_name("selected[]").get_attribute("value")
                self.__group_cache.append(Group(name=name, id=group_id))
        return list(self.__group_cache)

    def _select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def _select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector(f"input[value='{id}']").click()

    def _select_first_group(self):
        self._select_group_by_index(0)

    def _fill_group_form(self, group: Group):
        self._change_field("group_name", group.name)
        self._change_field("group_header", group.header)
        self._change_field("group_footer", group.footer)