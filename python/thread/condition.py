# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------   
# Author:  chenhao
# Date:  2020-08-15
# Description: 使用条件进行线程同步
#-------------------------------------------------------------------------------
from threading import Thread, Condition
import time

items = []
condition = Condition()

class consumer(Thread):
    def __init__(self):
        Thread.__init__(self)
    def consume(self):
        global condition
        global itmes
        condition.acquire()
        if len(items) == 0:
            condition.wait()
            print('consumer notify: no item to consume')
        items.pop()
        print('consumer notify: consumed 1 item')
        print('consumer notify: items to consum are {}'.format(len(items)))
        condition.notify()
        condition.release()
    def run(self):
        for i in range(20):
            time.sleep(2)
            self.consume()
class producer(Thread):
    def __init__(self):
        Thread.__init__(self)

    def produce(self):
        global condition
        global items

        condition.acquire()
        if len(items) == 10:
            condition.wait()
            print('producer notify: items producted are {}'.format(len(items)))
            print('producer notify: stop the production')
        items.append(1)
        print('producter notify : total itmes {}'.format(len(items)))
        condition.notify()
        condition.release()

    def run(self):
        for i in range(20):
            time.sleep(1)
            self.produce()

if __name__ == "__main__":
    producer = producer()
    consumer = consumer()

    producer.start()
    consumer.start()
    producer.join()
    consumer.join()












