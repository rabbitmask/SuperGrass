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


class Robots(HeadersClass):
    def run(self):
        payload = "/robots.txt"
        vulnurl = self.url + payload
        try:
            req = requests.get(vulnurl, headers=self.headers, timeout=5)
            if "Disallow" in req.text or "Allow" in req.text:
                return "[+]存在robots.txt爬虫文件...(敏感信息)"+"\tpayload: "+vulnurl
            else:
                pass
        except:
            pass

if __name__ == '__main__':
    r=Robots("http://www.zjswzm.com")
    r.run()