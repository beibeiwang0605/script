# -*- coding: utf-8 -*-
# Time ： 2020/4/12 23:37
# Auth ： beibei
import json

import requests
import yaml
from jsonpath import jsonpath


class BaseApi:
    params = {}
    data = {}

    def encode_base64(self):
        pass

    def decode_base64(self, content):
        # todo:把加密后的内容，解密，并生成一个结构化的数据
        return content

        # 封装yaml文件的加载

    @classmethod
    def yaml_load(cls, path) -> list:
        with open(path, encoding='utf-8') as f:
            return yaml.safe_load(f)

    # todo : staticmethod和classmethod区别,没有用到任何类变量，所以可以使用staticmethod
    # @staticmethod
    # def yaml_load(path) -> list:
    #     with open(path, encoding='utf-8') as f:
    #         return yaml.safe_load(f)

    def api_load(self, path):
        return self.yaml_load(path)

    def api_send(self, data=dict):
        # data['params']['access_token'] = self.get_token(self.secret)
        print(data)

        # todo:加密
        # req['xx']=self.encode_base64()

        # dump可以把之前的值存起来，序列流
        raw = yaml.dump(data)
        print(raw)
        for key, value in self.params.items():
            raw = raw.replace(f'${{{key}}}', repr(value))
            print('replace')
        # 把序列流转换成python object
        data = yaml.load(raw)
        print(data)

        # todo: 模板解析
        # for key,value in self.params.items():
        # #todo:递归
        #     for k,v in req['params'].items():
        #         if isinstance(v,str):
        #             req['params'][k]=v.replace(f"${k}", req['params'][k])
        #     print(req)

        # if isinstance(req['params'],dict):
        #     for k in req['params'].keys:
        #         req['params'][k]=req['params'][k]

        r = requests.request(
            method=data['method'],
            url=data['url'],
            params=data['params'],
            json=data.get('json')   # data.get()如果没有json可能会报错，和data['json']相比
        )
        self.format(r)
        # todo:解密
        # return self.decode_base64(r.content)
        return r.json()

    # todo :封装类似HttpRunner这样的数据驱动框架
    def steps_run(self, steps: list):

        for step in steps:
            print(step)
            # todo:使用format
            raw = yaml.dump(step)
            for key, value in self.params.items():
                # value有可能是数组，使用repr强制转换成str
                raw.replace(f'${{{key}}}', repr(value))
                print('replace')
                print(raw)
            req = yaml.safe_load(raw)

            if isinstance(step, dict):
                if 'method' in step.keys():
                    method = step['method'].split('.')[-1]
                    print(method)
                    getattr(self, method)(**step)
                    print(getattr(self, method)(**step))
                if 'extract' in step.keys():
                    # self.data[step['extract']]=getattr(self, 'jsonpath')(**step)
                    self.data[step['extract']] = getattr(self, 'jsonpath')(*step)
                    print("extract")
                    print(self.data[step['extract']])
                if "assertion" in step.keys():
                    assertion = step["assertion"]
                    if isinstance(assertion, str):
                        assert eval(assertion)
                    if assertion[1] == 'eq':
                        assert assertion[0] == assertion[2]

        # req['params']['access_token'] = self.get_token()
        # print(req)
        #
        # raw = yaml.dump(req)
        # for key, value in self.params.items():
        #     raw.replace(f'${{{key}}}', repr(value))
        #     print('replace')
        # req = yaml.safe_load(raw)

        # todo: 模板解析
        # for key,value in self.params.items():
        # #todo:递归
        #     for k,v in req['params'].items():
        #         if isinstance(v,str):
        #             req['params'][k]=v.replace(f"${k}", req['params'][k])
        #     print(req)

        # if isinstance(req['params'],dict):
        #     for k in req['params'].keys:
        #         req['params'][k]=req['params'][k]

        # r = requests.request(
        #     req['method'],
        #     url=req['url'],
        #     params=req['params'],
        #     json=req['json']
        # )
        # self.format(r)
        # return r.json()

    @classmethod
    def format(cls, r):
        cls.r = r   # 类方法，可能会有并发
        # ensure_ascii=False增加这个响应可以识别中文，不然打印出来是unicode编码
        result = json.dumps(r.json(), indent=2, ensure_ascii=False)
        print(result)
        # 下面的这个更好，直接转序列化和反序列化
        # print(json.dumps(json.loads(r.text), indent=2, ensure_ascii=False))
        return result

    def jsonpath(self, path, r=None):
        if r is None:
            r = self.r.json()
        return jsonpath(r, path)
    # def jsonpath(self, r, path):
    #     return jsonpath(r, path)
