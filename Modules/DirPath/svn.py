#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\

'''
import re
import requests
from Config.config_class import HeadersClass


class Svn(HeadersClass):
    def run(self):
        payload = "/.svn/entries"
        vulnurl = self.url + payload
        try:
            req = requests.get(vulnurl, headers=self.headers, timeout=10, allow_redirects=False)
            try:
                contents = str(req.text).split('\x0c')
                pattern = re.compile(r'has-props|file|dir')
                for content in contents:
                    match = len(pattern.search(content).group(0))
                    if req.status_code == 200 and match > 0:
                        return "[+]存在svn源码泄露漏洞...(高危)\tpayload: "+vulnurl
                pass
            except:
                pass
        except:
            pass