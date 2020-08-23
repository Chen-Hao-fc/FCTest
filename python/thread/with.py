# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------   
# Author:  chenhao
# Date:  2020-08-15
# Description:
#-------------------------------------------------------------------------------
import threading
import time

count1 = 1
count2 = 1
lock = threading.Lock()

def func1():
    global count1
    for i in range(10000):
        with lock:
        # lock.acquire()
            print('func1,count={}'.format(count1))
            # time.sleep(1)
            count1 += 1

        # lock.release()
def func2():
    global count1
    for i in range(10000):
        # print('func2,count={}'.format(count1))
        print('----------------------------------')
        # time.sleep(0.1)
        with lock:
        # lock.acquire()
            print('func2,count={}'.format(count1))
            count1 -= 1
        # lock.release()
if __name__ == "__main__":
    t1 = threading.Thread(target=func1)
    t2 = threading.Thread(target=func2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print('count1=', count1)
    print('count2=', count2)

