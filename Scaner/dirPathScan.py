#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\

'''
from multiprocessing import Manager,Pool
from Modules.DirPath.index import *


# def saveinfo(result):
#     if result:
#         fw=open(filename,'a')
#         fw.write(','+str(result))
#         fw.close()
#     else:
#         pass


def Scanwork(url,workname,q):
    res=eval(workname)(url).run()
    if res:
        print(res)
    q.put(workname)

def DirpathScan(url):
    p = Pool(10)
    q = Manager().Queue()
    for i in DirPathList:
        p.apply_async(Scanwork, args=(url,i,q,))
    p.close()
    p.join()


