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


class CrossDomain(HeadersClass):
    def run(self):
        payload = "/crossdomain.xml"
        vulnurl = self.url + payload
        try:
            req = requests.get(vulnurl, headers=self.headers, timeout=5)
            if r"<cross-domain-policy>" in req.text and r"allow-access-from" in req.text:
                return "[+]存在crossdomain.xml文件发现漏洞...(信息)\tpayload: "+vulnurl
            else:
                pass
        except:
            pass
