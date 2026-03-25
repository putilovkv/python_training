from selenium import webdriver
from fixture.navigation import NavigationHelper
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.entry import EntryHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "edge":
            self.wd = webdriver.Edge()
        else:
            raise ValueError(f"Unrecognized browser {browser}")
        self.navigation = NavigationHelper(self, base_url)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.entry = EntryHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()
