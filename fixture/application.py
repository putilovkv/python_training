from selenium import webdriver
from fixture.navigation import NavigationHelper
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.entry import EntryHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.navigation = NavigationHelper(self)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.entry = EntryHelper(self)

    def destroy(self):
        self.wd.quit()
