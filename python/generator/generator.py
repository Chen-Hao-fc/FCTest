# -*- coding: utf-8 -*-      
#--------------------------------------------
# Author:chenhao
# Date:2020-11-22 16:21
# Description:  
#--------------------------------------------

#生成器函数
def func1():
    for i in range(10):
        yield i

a = func1()
print(a)
for i in a:
    print(i)

#生成器表达式
b = (i for i in range(10))
print(b)
for i in b:
    print(i)
