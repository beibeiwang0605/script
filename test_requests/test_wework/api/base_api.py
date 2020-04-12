# -*- coding: utf-8 -*-
# Time ： 2020/4/12 23:37
# Auth ： beibei
import json
import logging

import yaml
from requests import Request


class BaseApi:
    # todo :封装类似HttpRunner这样的数据驱动框架
    def steps_yaml(self,path):
        with open(path) as f:
            steps:list[dict] = yaml.safe_load(f)
            request: Request= None
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
    @classmethod
    def format(cls, r):
        print(json.dumps(r.json(),indent=2))