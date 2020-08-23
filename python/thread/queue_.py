# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------   
# Author:  chenhao
# Date:  2020-08-16
# Description:
#-------------------------------------------------------------------------------
from multiprocessing import Queue
# import queue as Queue
# import Queue
from threading import Thread

import time
import random

class producer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
    def run(self):
        for i in range(10):
            item = random.randint(0, 256)
            self.queue.put(item)
            print('producer notify item: {} append to queue by {}'.format(item, self.name))
            time.sleep(1)
class consumer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
    def run(self):
        while True:
            item = self.queue.get()
            print('consumer notify item {} pop to queue by {}'.format(item, self.name))
            self.queue.task_done()

if __name__ == '__main__':
    queue = Queue()
    t1 = producer(queue)
    t2 = consumer(queue)
    t3 = producer(queue)
    t4 = consumer(queue)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()



