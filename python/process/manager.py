# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------   
# Author:  chenhao
# Date:  2020-08-23
# Description:
#-------------------------------------------------------------------------------
import multiprocessing
import time
def worker(dic, key, item):
    dic[key] = item
    time.sleep(1)
    print('key=%d value=%d' % (key, item), 'dic=', dic)


if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    dic = mgr.dict()
    jobs = [multiprocessing.Process(target=worker, args=(dic, i, i*2)) for i in range(10)]
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    print('result=', dic)