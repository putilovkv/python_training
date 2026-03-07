from fixture.base_helper import BaseHelper


class NavigationHelper(BaseHelper):

    home_page = "http://localhost/addressbook"

    def open_home_page(self):
        wd = self.app.wd
        wd.get(self.home_page)

    def go_to_home_page(self):
        wd = self.app.wd
        if wd.current_url.rstrip('/') != self.home_page or not wd.current_url.endswith("/index.php"):
            wd.find_element_by_link_text("home").click()

    def go_to_groups_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/groups.php") or len(wd.find_elements_by_name("new")) == 0:
            wd.find_element_by_link_text("groups").click()