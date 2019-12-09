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

headers = {'user-agent': 'Mozilla/5.1 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0', }


def submit():

    headers = {'user-agent': 'Mozilla/5.1 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',}

    def run(username):
        response=requests.get("url"+str(username),headers=headers)
        r=response.text
        # print(r)
        if re.search(r'keyword', r):
            return 1
        else:
            return 0


if __name__ == '__main__':
    print(run('username'))