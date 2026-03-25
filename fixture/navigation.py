from fixture.base_helper import BaseHelper


class NavigationHelper(BaseHelper):

    def __init__(self, app, base_url):
        super().__init__(app)
        self.base_url = base_url

    def open_home_page(self):
        wd = self.app.wd
        wd.get(self.base_url)

    def go_to_home_page(self):
        wd = self.app.wd
        if wd.current_url.rstrip('/') != self.base_url or not wd.current_url.endswith("/index.php"):
            wd.find_element_by_link_text("home").click()

    def go_to_groups_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/groups.php") or len(wd.find_elements_by_name("new")) == 0:
            wd.find_element_by_link_text("groups").click()