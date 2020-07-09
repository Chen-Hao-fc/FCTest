# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------   
# Author:  chenhao
# Date:  2020/7/4
# Email:  chenhao6@360.cn
# Description:
#-------------------------------------------------------------------------------
def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)
g = foo()
print(next(g))
print("*"*20)
print(next(g))
print('-'*20)
print(g.send(7))

def func():
    num = 0
    while True:
        print('num=', num)
        yield num
        num += 1

g = func()
print(next(g))
print('-'*10)
print(next(g))
import time
for i in g:
    time.sleep(2)
    print(i)