from appium import webdriver
def init_driver():
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
    return driver