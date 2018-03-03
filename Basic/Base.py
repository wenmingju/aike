from selenium.webdriver.support.wait import WebDriverWait
class Base(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, loc, timeout=5, poll=0.2):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    def click_element(self, loc):
        self.find_element(loc).click()

    def elment_sendkeys(self, loc, content):
        self.find_element(loc).send_keys(content)

    def find_toast(self, message, timeout=3, poll=0.2):
        messag = "//*[contains(@text,'{}')]".format(message)
        element = WebDriverWait(self.driver, timeout, poll).until(lambda y: y.find_element_by_xpath(messag))
        return element.text
