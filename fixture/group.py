from fixture.base_helper import BaseHelper
from model.group import Group


class GroupHelper(BaseHelper):

    def create(self, group: Group):
        wd = self.app.wd
        self.app.navigation.go_to_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self._fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
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
        self.app.navigation.go_to_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.app.navigation.go_to_groups_page()
        self._select_first_group()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.app.navigation.go_to_groups_page()

    def count(self):
        wd = self.app.wd
        self.app.navigation.go_to_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    def _select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def _fill_group_form(self, group: Group):
        self._change_field("group_name", group.name)
        self._change_field("group_header", group.header)
        self._change_field("group_footer", group.footer)