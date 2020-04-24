# -*- coding: utf-8 -*-
# Time ： 2020/4/10 19:25
# Auth ： beibei
# 导入包的时候要导入对
import logging

import yaml
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


def exception_handle(fun):
    def magic(*args, **kwargs):
        _self: BasePage = args[0]
        try:
            result = fun(*args, **kwargs)
            # 清空计数次数
            return result
        except Exception as e:
            # 加计数，避免抛异常进入死循环，如果次数太多，就退出异常逻辑，直接报错，抛异常
            if _self._error_count >= _self._error_max:
                raise e
            _self._error_count += 1
            # 对黑名单里的弹框进行处理
            for element in _self._black_list:
                elements = _self._driver.find_elements(*element)
                if len(elements) > 0:
                    elements[0].click()
                    break
            # return 继续寻找原来正常的控件
            return magic(*args, *kwargs)
    return magic

class BasePage:
    # 加日志功能，可以打印一些异常信息
    logging.basicConfig(level=logging.INFO)
    _driver: WebDriver
    # 黑名单
    _black_list = [
        (By.ID, "tv_agree"),
        (By.XPATH, '//*[@text="确定"]'),
        (By.ID, 'image_cancel'),
        (By.XPATH, '//*[@text="下次再说"]')
    ]
    _error_max = 5
    _error_count = 0
    _params={}

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    @exception_handle
    def find_element(self, by, locator: str = None):
        return self._driver.find_element(*by) if isinstance(by, tuple) else self._driver.find_element(by, locator)

    @exception_handle
    def sendkeys(self,value, by, locator=None):
        return self.find_element(by,locator).send_keys(value)

    @exception_handle
    def find_and_get_text(self, by, locator: str = None):
        logging.info(by)
        logging.info(locator)
        element = self.find_element(by, locator)
        return element.text

    """获取弹框toast"""
    def get_toast(self):
        return self.find_element(By.XPATH, "//*[@class='android.widget.Toast']").text

    def text(self, key):
        return (By.XPATH, "//*[@text='%s']" % key)

    def find_by_text(self, key):
        return self.find_element(self.text(key))

    def yaml(self,path):
        print(yaml.safe_load(open(path)))

    def steps_yaml(self,path):
        # 加utf-8防止乱码
        with open(path,encoding="utf-8") as f:
            #读取步骤定义文件
            steps: list[dict] = yaml.safe_load(f)
            #保存一个目标对象
            # element: WebElement= None
            for step in steps:
                logging.info(step)
                print(step)
                if "by" in step.keys():
                    element = self.find_element(step["by"],step["locator"])
                if "action" in step.keys():
                    if step["action"] == "click":
                        element.click()
                    if step["action"] in ["send","input"] :
                        content: str = step["value"]
                        for param in self._params.keys():
                            # value: jd, value2:jd
                            content = content.replace("{%s}"%param, self._params[param])
                        element.send_keys(content)
                    if step["action"] == "text":
                        element.text()
                    if step["action"] == "attribute":
                        element.get_attribute(step["value"])



