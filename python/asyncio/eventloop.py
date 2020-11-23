# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------   
# Author:  chenhao
# Date:  2020-08-30
# Description:
#-------------------------------------------------------------------------------
import asyncio
import datetime
import time

def func_1(end_time, loop):
    print("func_1 called")
    if(loop.time() + 1.0) < end_time:
        loop.call_later(1, func_2, end_time, loop)
    else:
        loop.stop()

def func_2(end_time, loop):
    print("fun_2 called")
    if(loop.time() + 1.0) < end_time:
        loop.call_later(1, func_3, end_time, loop)
    else:
        loop.stop()

def func_3(end_time, loop):
    print("fun_3 called")
    if(loop.time() + 1.0) < end_time:
        loop.call_later(1, func_1, end_time, loop)
    else:
        loop.stop()

def func_4(end_time, loop):
    print("func_5 called")
    if(loop.time() + 1.0) < end_time:
        loop.call_later(1, func_4, end_time, loop)
    else:
        loop.stop()
loop = asyncio.get_event_loop()
print(loop.time())
end_loop = loop.time() + 9.0
print(end_loop)
loop.call_soon(func_1, end_loop, loop)
print(loop.time())
loop.run_forever()
loop.close()