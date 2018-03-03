import Page
from Basic.Base import Base
class Login(Base):
    def __init__(self, driver):
            Base.__init__(self, driver)

    def input_phone(self, phone_number):
        self.elment_sendkeys(Page.phone, phone_number)

    def input_password(self, login_password):
        self.elment_sendkeys(Page.password, login_password)

    def click_login_button(self):
        self.click_element(Page.login_buton)

