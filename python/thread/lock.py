# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------   
# Author:  chenhao
# Date:  2020-08-15
# Description:
#-------------------------------------------------------------------------------
import threading

shared_resource_with_lock = 0
shared_resource_with_no_lock = 0
COUNT= 100000

shared_resource_lock = threading.Lock()

def increment_with_lock():
    global shared_resource_with_lock
    for _ in range(COUNT):
        shared_resource_lock.acquire()
        shared_resource_with_lock += 1
        print('in={}'.format(shared_resource_with_lock))
        shared_resource_lock.release()

def decrement_with_lock():
    global shared_resource_with_lock
    for _ in range(COUNT):
        shared_resource_lock.acquire()
        shared_resource_with_lock -= 1
        print('de={}'.format(shared_resource_with_lock))
        shared_resource_lock.release()


def increment_without_lock():
    global shared_resource_with_no_lock
    for _ in range(COUNT):
        shared_resource_with_no_lock += 1

def decrement_without_lock():
    global shared_resource_with_no_lock
    for _ in range(COUNT):
        shared_resource_with_no_lock -= 1

if __name__ == '__main__':
    t1 = threading.Thread(target = increment_with_lock)
    t2 = threading.Thread(target = decrement_with_lock)
    # t3 = threading.Thread(target = increment_without_lock)
    # t4 = threading.Thread(target = decrement_without_lock)
    t1.start()
    t2.start()
    # t3.start()
    # t4.start()
    t1.join()
    t2.join()
    # t3.join()
    # t4.join()

    print('with lock {}'.format(shared_resource_with_lock))

    print('without lock {}'.format(shared_resource_with_no_lock))









