# -*- coding: utf-8 -*-
# Time ： 2020/4/4 12:14
# Auth ： beibei
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestXueqiu:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "Android 6.0"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["automationName"] = "uiautomator2"
        caps["noReset"] = True  # Ture表示不重置，False表示重置，数据被清理的过程
        # caps["dontStopAppOnReset"] = True
        caps["unicodeKeyboard"] = True  # 是否需要输入非英文之外的语言，True表示"是“
        caps["resetKeyBoard"] = True
        caps['autoGrantPermissions'] = True   # 让appium自动授权app权限，如果noReset为True，则该条不生效。
        # caps["chromedriverExecutableDir"] = "D:/test/chromedriver"
        caps["chromedriverExecutable"] = "D:/test/chromedriver/chrome_43.0.2357.0/chromedriver_2.20.exe"    # 指定chromedriver
        caps["avd"] = 'Android_9.0'    #可以指定模拟器启动并运行

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)
        # WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located())   # 显式等待
        # try:
        #     self.driver.find_element(By.XPATH, '//*[text="同意"]').click()
        # finally:
        #     pass

    def test_search(self):
        # self.driver.implicitly_wait(10)    #隐式等待
        # el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_agree")
        # el1.click()
        # self.driver.find_element(MobileBy.ID,"tv_agree").click()   # 这种方法可以自动补全id前面的信息
        # el2 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        # el2.click()
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        # el3 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        # el3.send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys('阿里巴巴')

    def test_search_and_get_price(self):
        # self.driver.find_element(MobileBy.ID,"tv_agree").click()
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys('阿里巴巴')
        self.driver.find_element(MobileBy.ID, "name").click()
        assert float(self.driver.find_element(MobileBy.ID, 'current_price').text) > 100

    def test_search_and_get_price_hk(self):
        """找到阿里巴巴的股票，并断言价格小于200"""
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys('alibaba')
        # self.driver.find_element(MobileBy.ID,'fl_container').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="阿里巴巴"]').click()
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="股票"]').click()
        # 股票的文本不唯一，其他地方也有可能使用，所以要先找到父节点
        stock = (By.XPATH, '//*[contains(@resource-id,"title_container")]//*[@text="股票"]')
        self.driver.find_element(*stock).click()
        # self.driver.find_element(MobileBy.XPATH,'//*[@text="09988"]').click()

        # 高级xpath定位（空间），根据子节点找到父节点，/..表示父节点, //代表子孙元素
        price = (By.XPATH, '//*[@text="09988"]/../../..//*[contains(@resource-id,"current_price")]')
        assert float(self.driver.find_element(*price).text) < 200
        print(self.driver.find_element(*price).get_attribute("resource-id"))

    def test_search_and_add_select(self):
        """雪球app，搜索阿里巴巴，加自选后断言"""
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys('阿里巴巴')
        self.driver.find_element(MobileBy.ID, "name").click()
        time.sleep(2)
        select = (MobileBy.XPATH, '//*[@text="09988"]/../../..//*[contains(@resource-id,"follow_btn")]')
        self.driver.find_element(*select).click()
        self.driver.find_element(MobileBy.ID, 'tv_left').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="取消"]').click()
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        # self.driver.hide_keyboard() #隐藏键盘
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys('阿里巴巴')
        self.driver.find_element(MobileBy.ID, "name").click()
        select_ok = (By.XPATH, '//*[@text="09988"]/../../..//*[contains(@resource-id,"followed_btn")]')
        assert "已添加" in self.driver.find_element(*select_ok).get_attribute("text")

    def test_scroll(self):
        size = self.driver.get_window_size()  # 互殴去屏幕的宽度和高度，字典类型，比如{'width': 1080, 'height': 1794}
        # 滑动手机屏幕，从下往上滑,for循环可以滑动10次
        for i in range(10):
            TouchAction(self.driver).long_press(x=size['width'] * 0.5, y=size['height'] * 0.8). \
                move_to(x=size['width'] * 0.5, y=size['height'] * 0.2).release().perform()

    def test_device(self):
        self.driver.background_app(5)  # 放到后台5s
        self.driver.lock(5)  # 锁屏5s
        self.driver.unlock()  # 解锁

    def test_resource(self):
        print(self.driver.page_source)  # 可以获取到页面源码xml格式,跟爬虫有点相似，获取到页面资源，提取出我们需要的信息
        # 非贪婪匹配，匹配所有满足'target="_blank">....</a></h2>'格式的信息，结果显示是一个列表
        # self.titles = re.findall(r'target="_blank">(.*?)</a></h2>', self.page)
        # for title in self.titles:
        #    print(title)

    def test_xpath(self):
        # 高级xpath定位（空间），根据子节点找到父节点，/..表示父节点
        self.driver.find_element(By.XPATH,
                                 '//*[@text="09988"]/../../..//*[contains(@resource-id,"current_price")]').click()

    def test_uiselector(self):
        # 高级定位uiselector ,只适用于安卓
        # https://blog.csdn.net/aliuti/article/details/79628967
        self.driver.find_element(By.XPATH, '//*[@text="推荐"]').click()
        scroll_to_element = (MobileBy.ANDROID_UIAUTOMATOR,
                             'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                             '.scrollIntoView(new UiSelector().text("1小时前").instance(0));')
        self.driver.find_element(*scroll_to_element).click()

    def test_webview_native(self):
        """原生的app页面，用android 9.0可以调试通过"""
        self.driver.find_element(By.XPATH, '//*[@text="交易" and contains(@resource-id,"tab_name")]').click()
        # self.driver.find_element(MobileBy.ACCESSIBILITY_ID,'A股开户').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="A股开户"]').click()
        # self.driver.find_element(MobileBy.XPATH,'//*[@class="android.widget.EditText" and contains(@resource-id,"phone-number")]').send_keys("18292861564")
        # phone=(MobileBy.ACCESSIBILITY_ID,'输入11位手机号')
        phone = (MobileBy.XPATH, '//*[@class="android.widget.EditText" and contains(@resource-id,"phone-number")]')
        WebDriverWait(self.driver, 50).until(expected_conditions.element_to_be_clickable(phone))
        self.driver.find_element(*phone).click()
        # 如果找不到元素，可以尝试打印，使用get_attribute看是否可以打印出来
        # print(self.driver.find_element(*phone).get_attribute("content-desc"))
        # print(self.driver.page_source)
        # time.sleep(10)
        # print(self.driver.page_source)
        self.driver.find_element(*phone).send_keys("18292861564")
        # for element in self.driver.find_elements(*phone):
        #     try:
        #         # element.click()
        #         element.send_keys("18292861564")
        #     except Exception as e:
        #         print(element.get_attribute("class"))
        #         print(element.get_attribute("resource-id"))
        #         print(element.get_attribute("content-desc"))
        #         print(e)

    def test_webview_context(self):
        """，切换上下文到webview"""
        self.driver.find_element(By.XPATH, '//*[@text="交易" and contains(@resource-id,"tab_name")]').click()
        # for i in range(5):
        #     print(self.driver.contexts)
        #     time.sleep(1)
        # print(self.driver.page_source)
        # 等待上下文出现，切上下文，意思是原生和webview之间的切换
        # 坑1：webview上下文出现大概3s的延迟，加显式等待，android6.0的系统才可以支持，其他的需要打开webview调试开关
        # adb shell cat /proc/net/unix | findstr "webview" # 找webview相关的进程，有一个webview就会算到上下文里
        WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.contexts) > 1)
        # 坑2：chrome的版本必须和chromedriver的版本必须对应
        # 坑3：chromedriver可能会存在无法对应chrome的版本的情况，需要使用caps的mapping file或者直接chromedriverExecutable
        # chromedriver D:/test/chromedriver/chrome_43.0.2357.0/chromedriver_2.20.exe --url-base=wd/hub --port=8000 --adb-port=5037 --verbose
        webview = self.driver.contexts[-1]
        self.driver.switch_to.context(webview)
       #  print(self.driver.page_source)
        # print(self.driver.window_handles)

        # 上下文切换之后，就可以使用h5(html)定位元素
        origin_handles = len(self.driver.window_handles)
        # 使用chrome inspect分析界面控件chrome://inspect/#devices，需要代理、需要chrome62及以前的版本，
        # Proxying [POST /wd/hub/session/51a5dc86-835d-4e8a-994d-f56ac75731ec/element] to [POST http://127.0.0.1:8000/wd/hub/session/7ddfbd071c17aac70762d069e9283397/element] with body: {"using":"css selector","value":".trade_home_info_3aI"}
        self.driver.find_element(By.CSS_SELECTOR, '.trade_home_info_3aI').click()
        # 首次做测试，需要分析当前窗口，打印有几个窗口,看是否需要切换窗口才可以找到元素
        # for i in range(5):
        #     print(self.driver.window_handles)
        #     time.sleep(0.5)
        # webview需要切换窗口,和之前的windows_hangdles个数做比较

        # 坑4：可能会出现多窗口，所以要注意切换
        WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.window_handles) > origin_handles)
        hanldle = self.driver.window_handles[-1]
        self.driver.switch_to.window(hanldle)
        phone = (By.ID, 'phone-number')
        # html定位的常见问题，元素可以找到的时候，不代表可以叫胡，需要显式等待
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(phone))
        self.driver.find_element(*phone).send_keys("18292861564")

    def test_xueying(self):
        """港美股开户->输入手机号与错误的验证码 1234->点击开户->切换回原生->点击关闭回到交易页"""
        print(self.driver.contexts)
        self.driver.find_element(By.XPATH, '//*[@text="交易" and contains(@resource-id,"tab_name")]').click()
        # 切换到webview
        WebDriverWait(self.driver,20).until(lambda x : len(self.driver.contexts) > 1)
        print(self.driver.contexts)
        webview = self.driver.contexts[-1]
        self.driver.switch_to.context(webview)
        # 点吉港美股开户
        print(self.driver.window_handles)
        handles = len(self.driver.window_handles)
        self.driver.find_element(By.CSS_SELECTOR,'.trade_home_xueying_SJY .trade_home_info_3aI').click()
        # WebDriverWait(self.driver,20).until()
        print(self.driver.window_handles)
        # 切换windows_handles窗口,输入手机号、验证码，点击立即开户
        WebDriverWait(self.driver, 20).until(lambda  x : len(self.driver.window_handles) > handles )
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # html定位的常见问题，元素可以找到的时候，不代表可以叫胡，需要显式等待
        phone = (By.CSS_SELECTOR,'[placeholder="请输入手机号"]')
        WebDriverWait(self.driver,30).until(expected_conditions.element_to_be_clickable(phone))
        self.driver.find_element(*phone).send_keys("18292861564")
        self.driver.find_element(By.CSS_SELECTOR,'[placeholder="请输入验证码"]').send_keys("1234")
        self.driver.find_element(By.CSS_SELECTOR,'.open_form-submit_1Ms').click()
        # 切换回原生
        self.driver.switch_to.context(self.driver.contexts[0])
        self.driver.find_element(MobileBy.ID,'action_bar_close').click()

    def test_avd(self):
        self.driver.find_element(By.XPATH, '//*[@text="行情"]').click()

    def test_performance(self):
        """打印性能数据cpu、内存、电池、网络"""
        for p in self.driver.get_performance_data_types():
            print(p)
            if p != "cpuinfo":
               print(self.driver.get_performance_data("com.xueqiu.android", p, 10))

    def test_record(self):
        #录屏，scrcpy更好用的录屏工具
        self.driver.start_recording_screen()

        self.driver.find_element(By.XPATH, '//*[@text="交易" and contains(@resource-id,"tab_name")]').click()
        # self.driver.find_element(MobileBy.ACCESSIBILITY_ID,'A股开户').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="A股开户"]').click()
        # self.driver.find_element(MobileBy.XPATH,'//*[@class="android.widget.EditText" and contains(@resource-id,"phone-number")]').send_keys("18292861564")
        # phone=(MobileBy.ACCESSIBILITY_ID,'输入11位手机号')
        phone = (MobileBy.XPATH, '//*[@class="android.widget.EditText" and contains(@resource-id,"phone-number")]')
        WebDriverWait(self.driver, 50).until(expected_conditions.element_to_be_clickable(phone))
        self.driver.find_element(*phone).click()
        # 如果找不到元素，可以尝试打印，使用get_attribute看是否可以打印出来
        # print(self.driver.find_element(*phone).get_attribute("content-desc"))
        # print(self.driver.page_source)
        # time.sleep(10)
        # print(self.driver.page_source)
        self.driver.find_element(*phone).send_keys("18292861564")
        self.driver.stop_recording_screen()

    def test_shell(self):
        """执行一些shell脚本，运行时需要加上appium -g D://tmp/appium.log --relaxed-security"""
        result = self.driver.execute_script('mobile: shell', {
            'command': 'ps',
            'args': [],
            'includeStderr': True,
            'timeout': 5000
        })
        # assert result['stdout'] == 'arg1 arg2'
        print(result)
    def teardown(self):
        time.sleep(10)
        self.driver.quit()
