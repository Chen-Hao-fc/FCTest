# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------   
# Author:  chenhao
# Date:  2020-08-30
# Description: 主要介绍 current.Features模块
#-------------------------------------------------------------------------------
import concurrent.futures

import time
number_list = range(1, 11)
def evalute_item(x):
    result_item = count(x)
    return result_item

def count(number):
    for i in range(0, 10000000):
        i += 1
    return i * number
if __name__ == '__main__':
    start_time = time.time()
    for item in number_list:
        print(evalute_item(item))
    print("sequential execution in" + str(time.time() - start_time), "seconds")

    start_time_1= time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(evalute_item, item) for item in number_list]
        for future in concurrent.futures.as_completed(futures):
            print(future.result())
    print("Thread pool execution in " + str(time.time() - start_time_1), "seconds")

    start_time_2 = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(evalute_item, item) for item in number_list]
        for future in concurrent.futures.as_completed(futures):
            print(future.result())
    print("Process pool execution in " + str(time.time() - start_time_2), "seconds")
# print(evalute_item(10))