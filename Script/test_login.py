import pytest,allure
from Page.Pages import Page
from Basic.init_driver import init_driver
from Basic.Read_data import read_data
def read_login_data():
        data_list = []
        data = read_data("data_login").get("Logindata")
        for i in data.keys():
            data_list.append((data.get(i).get("phone"), data.get(i).get("passwd"), data.get(i).get("expect"),data.get(i).get("toast")))
        return data_list

class Test_login(object):
        def setup_class(self):
            self.driver = init_driver()
            self.login_obj = Page(self.driver).page_login()

        def teardown_class(self):
            self.driver.quit()

        @allure.step('我是测试步骤001')
        @pytest.mark.parametrize("phone, passwd, expect, toast", read_login_data())
        def test_login(self,phone, passwd, expect, toast):
                self.login_obj.input_phone(phone)
                self.login_obj.input_password(passwd)
                self.login_obj.click_login_button()
                get_toast = self.login_obj.find_toast(expect)
                assert get_toast == toast