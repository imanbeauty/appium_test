from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = '127.0.0.1:62001'
desired_caps['appPackage'] = 'com.sankuai.meituan'
desired_caps['appActivity'] = '.activity.Welcome'
desired_caps['autoAcceptAlerts'] = 'True'   # 自动确认弹窗
desired_caps['unicodeKeyboard'] = 'True'    #处理无法输入中文的问题,使用unicodeKeyboard的编码方式来发送字符串
desired_caps['resetKeyboard'] = 'True'      #将键盘给隐藏起来
d = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(3)               # app启动后等待3秒，方便元素加载完成
d.find_element_by_id('com.sankuai.meituan:id/citylist_search').send_keys('深圳')
time.sleep(3)
d.find_element_by_id('com.sankuai.meituan:id/citylist_textview').click()
time.sleep(3)
d.tap([(75, 400)])
time.sleep(3)       # 临时取消弹框
d.tap([(0,270),(180,450)],500)
time.sleep(3)       # 定位元素美食，按住500毫秒
d.tap([(218,406)])  # 定位商家
time.sleep(2)
d.tap([(163,754)])  # 查看商品详情
time.sleep(2)
d.find_element_by_id("com.sankuai.meituan:id/buy").click()   #立即购买
d.find_element_by_id("com.sankuai.meituan:id/mobile").send_keys("15623512919")      # 输入手机号
d.find_element_by_id("com.sankuai.meituan:id/get_code").click()             # 获取验证码
#异常处理（解决有时候需要输入图片验证码，有时候又不需要输入的问题）
try:
    print('请输入图片验证码')
    picutrecode = input()
    d.find_element_by_id('com.sankuai.meituan:id/captcha').send_keys(picutrecode)
    d.find_element_by_class_name('android.widget.Button').click()
    time.sleep(5)
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
    time.sleep(2)
# 通过查找不到元素从而报错来判断是否登录成功（相当于断言）
try:
    d.find_element_by_id('com.sankuai.meituan:id/submit').click()
    print('登录下单成功啦')
except:
    d.find_element_by_id('android:id/button1').click()
    print('登录失败啦')
d.get_screenshot_as_file(u'F:\自动化截图\美团.png')  #是否登录成功截图
d.find