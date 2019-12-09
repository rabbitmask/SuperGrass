#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\

'''
import requests
from Config.config_class import HeadersClass


class OptionsMethod(HeadersClass):
    def run(self):
        vulnurl = self.url
        # try:
        req = requests.options(vulnurl, headers=self.headers, timeout=5)
        # print(req.headers)
        if r"OPTIONS" in req.headers['Allow']:
            return "[+]存在options方法开启...(敏感信息)"+"\tpayload: "+vulnurl+"\tAllow:"+req.headers['Allow']
        else:
            pass
        # except:
        #     pass


if __name__ == '__main__':
    r=OptionsMethod("http://www.zjswzm.com")
    print(r.run())