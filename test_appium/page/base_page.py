# -*- coding: utf-8 -*-
# Time ： 2020/4/10 19:25
# Auth ： beibei
# 导入包的时候要导入对
import logging

import yaml
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


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
    _error_max = 3
    _error_count = 0
    _params={}
    # 把app里的driver传递过来这里使用
    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    # TODO:当有广告、评价等各种弹框出现的时候，要进行异常流程处理
    def find_element(self, by, locator: str = None):
        logging.info(by)
        logging.info(locator)
        try:
            # 寻找控件
            # element=self._driver.find_element(*by) if isinstance(by, tuple) else self._driver.find_element(by, locator)
            if isinstance(by, tuple):
                return self._driver.find_element(*by)
            else:
                return self._driver.find_element(by, locator)
            # 如果成功，清空错误计数
            self._error_count = 0
            # return element
        except Exception as e:
            # 如果次数太多，就退出异常逻辑，直接报错，抛异常
            if self._error_count > self._error_max:
                raise e
            # 记录一直异常的次数
            self._error_count += 1
            # 对黑名单里的弹框进行处理
            for element in self._black_list:
                logging.info(element)
                elements = self._driver.find_elements(*element)
                if len(elements) > 0:
                    elements[0].click()
                    # 继续寻找原来正常的控件
                    return self.find_element(by, locator)
            # 如果黑名单也没有，就报错
            logging.warn("black list no one found")
            raise e
            # self._driver.back()
            # return  self.find_element(by,locator)

        # todo :通用异常，通过装饰器让函数自动处理异常

    def find_and_get_text(self, by, locator: str = None):
        logging.info(by)
        logging.info(locator)
        try:
            # 寻找控件
            element = self._driver.find_element(*by) if isinstance(by, tuple) else self._driver.find_element(by,
                                                                                                             locator)
            # if isinstance(by, tuple):
            #     return self._driver.find_element(*by)
            # else:
            #     return self._driver.find_element(by, locator)
            # 如果成功，清空错误计数
            self._error_count = 0
            return element.text
        except Exception as e:
            # 如果册数太多，就退出异常逻辑，直接报错，抛异常
            if self._error_count > self._error_max:
                raise e
            # 记录一直异常的次数
            self._error_count += 1
            # 对黑名单里的弹框进行处理
            for element in self._black_list:
                logging.info(element)
                elements = self._driver.find_elements(*element)
                if len(elements) > 0:
                    elements[0].click()
                    # 继续寻找原来正常的控件
                    return self.find_and_get_text(by, locator)
            # 如果黑名单也没有，就报错
            logging.warn("black list no one found")
            raise e
            # self._driver.back()
            # return  self.find_element(by,locator)

    def get_toast(self):
        """获取弹框toast"""
        return self.find_element(By.XPATH, "//*[@class='android.widget.Toast']").text

    def text(self, key):
        return (By.XPATH, "//*[@text='%s']" % key)

    def find_by_text(self, key):
        return self.find_element(self.text(key))

    def yaml(self,path):
        print(yaml.safe_load(open(path)))

    def steps_yaml(self,path):
        with open(path) as f:
            steps:list[dict] = yaml.safe_load(f)
            element: WebElement= None
            for step in steps:
                logging.info(step)
                if "by" in step.keys():
                    element=self.find_element(step["by"],step["locator"])
                if "action" in step.keys():
                    action=step["action"]
                    if action == "find_element":
                        pass
                    elif action =="click":
                        element.click()
                    elif action == "text":
                        element.text
                    elif action == "attribute":
                        element.get_attribute(step["value"])
                    elif action in ["send", "input"]:
                        content=step["value"]
                        for key in self._params.keys():
                            content=content.replace("{%s}" %key, self._params[key])
                        element.send_keys(content)


