from appium import webdriver
from time import sleep
def mobilephone(self):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4.2'
    desired_caps['deviceName'] = '127.0.0.1:62001'
    desired_caps['appPackage'] = 'com.sankuai.meituan'
    desired_caps['appActivity'] = '.city.CityActivity'
    desired_caps['unicodeKeyboard'] = 'True'
    desired_caps['resetKeyboard'] = 'True'
    self.d = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    sleep(3)

