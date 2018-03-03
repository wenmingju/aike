from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
#启动参数
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
desired_caps['automationName'] = 'Uiautomator2'
desired_caps['appPackage'] = 'com.vcooline.aike'
desired_caps['appActivity'] = '.activity.MainActivity'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_id("com.vcooline.aike:id/login_username_edit").send_keys("18321733141")
driver.find_element_by_id("com.vcooline.aike:id/login_password_edit").send_keys("123456")
driver.find_element_by_id("com.vcooline.aike:id/button_login").click()
message = "//*[contains(@text, '{}')]".format("帐号")
element = WebDriverWait(driver, 5, 0.2).until(lambda x: x.find_element_by_xpath(message))
print(element.text)
print(driver.context)
time.sleep(5)
driver.quit()

