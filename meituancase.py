import  unittest
from appium import webdriver
from time import sleep

class MeituanTest(unittest.TestCase):
    #手机初始化进入APP
    def setUp(self):
        print('开始跑用例啦--setup')
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

    #选择地区购买商品流程
    def test_goshopping(self):
        d = self.d
        d.find_element_by_id('com.sankuai.meituan:id/citylist_search').send_keys('深圳')
        sleep(3)
        d.find_element_by_id('com.sankuai.meituan:id/citylist_textview').click()
        sleep(3)
        d.tap([(75, 400)])
        sleep(3)  # 临时取消弹框
        d.tap([(0, 270), (180, 450)], 500)
        sleep(3)  # 定位元素美食，按住500毫秒
        d.tap([(218, 406)])  # 定位商家
        sleep(2)
        d.tap([(191, 654)])  # 查看商品详情
        sleep(2)
        d.find_element_by_id("com.sankuai.meituan:id/buy").click()  # 立即购买
        d.find_element_by_id("com.sankuai.meituan:id/mobile").send_keys("15623512919")  # 输入手机号
        d.find_element_by_id("com.sankuai.meituan:id/get_code").click()  # 获取验证码
        # 异常处理（解决有时候需要输入图片验证码，有时候又不需要输入的问题）
        try:
            print('请输入图片验证码')
            picutrecode = input()
            d.find_element_by_id('com.sankuai.meituan:id/captcha').send_keys(picutrecode)
            d.find_element_by_class_name('android.widget.Button').click()
            sleep(5)
        except:
            print('请输入短信验证码')
            code = input()
            d.find_element_by_id('com.sankuai.meituan:id/code').send_keys(code)
            d.find_element_by_id('com.sankuai.meituan:id/submit').click()
        else:
            print('在输入图片验证码后，请再次输入短信验证码')
            code = input()
            d.find_element_by_id('com.sankuai.meituan:id/code').send_keys(code)
            d.find_element_by_id('com.sankuai.meituan:id/submit').click()
            print('程序运行正常')
            sleep(2)
        # 通过查找不到元素从而报错来判断是否登录成功（相当于断言）# 是否登录成功校验
        try:
            d.find_element_by_id('com.sankuai.meituan:id/submit').click()
            print('登录下单成功啦')
        except:
            d.find_element_by_id('android:id/button1').click()
            print('登录失败啦')
        d.get_screenshot_as_file(u'F:\自动化截图\美团.png')  # 是否登录成功截图

    def tearDown(self):
        sleep(2)
        self.d.quit()
if __name__ == "__main__":
    unittest.main()