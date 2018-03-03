from Page.Page_login import Login
class Page(object):
    def __init__(self, driver):
        self.driver = driver

    def page_login(self):
        return Login(self.driver)
