# Generated by Selenium IDE
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.actions.mouse_button import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_selenium.test_hogwarts import TestHogwarts


class TestBrowser(TestHogwarts):
    def setup_method(self,method):
        browser = os.getenv("browser", "").lower()
        if browser == "PhantomJS":
            self.driver = webdriver.PhantomJS()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser=='headless':
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")   # 如果脚本运行顺畅，可以使用无界面运行
            options.add_argument("--disable-gpu")  # 禁用gpu加速
            options.add_argument("--window-size=1280,1696")   # 设置分辨率
            self.driver = webdriver.Chrome(options=options)
        elif browser=='reuse':
            options = webdriver.ChromeOptions()
            options.debugger_address="127.0.0.1:9222"    # 使用已经存在的chrome进程
            self.driver = webdriver.Chrome(options=options)
        else:
            options = webdriver.ChromeOptions()

            # self.driver = webdriver.Chrome(options.headless)  # 加option,headless可以使页面无显示加载
        # self.driver = webdriver.Firefox()
        #self.driver.set_window_size(1552, 840)
        self.driver.get("https://testerhome.com/")
        # 隐式等待
        self.driver.implicitly_wait(5)

    def wait(self, timeout, method):
        WebDriverWait(self.driver, timeout).until(method)

    def test_testseach(self):
        self.driver.find_element(By.LINK_TEXT, "社团").click()
        # todo:显示等待
        element = (By.PARTIAL_LINK_TEXT, '霍格沃兹测试学院')
        self.wait(30, expected_conditions.element_to_be_clickable(element))
        # WebDriverWait(self.driver,10).until((lambda x:self.driver.find_element(element)))
        self.driver.find_element(*element).click()  # *element拆箱，把一个元组拆成2个元素
        # 尽量使用css的定位方式，link有可能导致解析元素出现异常
        # 使用css比link更好用
        # self.driver.find_element(By.CSS_SELECTOR, '[data-name="霍格沃兹测试学院"]').click()
        # done:隐式等待
        self.driver.find_element(By.CSS_SELECTOR, '.topic:nth-child(1) .title a').click()

    def test_mtsc2020(self):
        self.driver.get("https://testerhome.com/topics/21805")
        self.driver.minimize_window()
        print(self.driver.window_handles)
        # self.driver.switch_to.frame(0)
        sub = (By.PARTIAL_LINK_TEXT, '第六届中国互联网测试开发大会')
        self.wait(40, expected_conditions.element_to_be_clickable(sub))
        self.driver.find_element(*sub).click()
        print(self.driver.window_handles)
        self.wait(40, lambda x: len(self.driver.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        sub2 = (By.LINK_TEXT, '演讲申请')
        self.driver.save_screenshot("1.png")   # 截图
        self.wait(50, expected_conditions.element_to_be_clickable(sub2))
        #WebDriverWait(self.driver, 50).until(expected_conditions.element_to_be_clickable(sub2))
        self.driver.find_element(*sub2).click()  # link_text经常会出现加载慢问题，可以加显示等待

    def test_js(self):
        # todo:专项测试的时候会讲如何获取性能
        for code in ["return document.title",
                     'return document.querySelector(".active").className',
                     'return JSON.stringify(performance.timing)']:
            result = self.driver.execute_script(code)
            print(result)

    def teardown_method(self):
        time.sleep(5)
        self.driver.quit()