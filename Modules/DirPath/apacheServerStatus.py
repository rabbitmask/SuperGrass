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


class ApacheServerStatus(HeadersClass):
    def run(self):
        payload = "/server-status"
        vulnurl = self.url + payload
        try:
            req = requests.get(vulnurl, headers=self.headers, timeout=5)
            if r"Server uptime" in req.text and r"Server Status" in req.text and req.status_code==200:
                return "[+]存在git源码泄露漏洞...(低危)\tpayload: "+vulnurl
            else:
                pass
        except:
            pass
