# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------   
# Author:  chenhao
# Date:  2020-08-15
# Description: #使用信号量同步线程
#-------------------------------------------------------------------------------
import threading
import time
import random

semaphore = threading.Semaphore(0) #初始设置为0

def consumer():
    print('consumer is waiting')
    semaphore.acquire()#如果semaphore为0 就会阻塞程序，直到得到另一个线程通知，而如果semaphore是一个大于0的数字，acquire这里就会-1
    print('consumer notify: consumer item numer {}'.format(item))
def producer():
    global item
    time.sleep(10)
    item = random.randint(0, 1000)
    print('producer notify  produced item number {}'.format(item))
    semaphore.release() #可以提高计数器，然后通知其他线程

if __name__ == '__main__':
    for _ in range(5):
        t1 = threading.Thread(target=producer)
        t2 = threading.Thread(target=consumer)

        t1.start()
        t2.start()
        t1.join()
        t2.join()