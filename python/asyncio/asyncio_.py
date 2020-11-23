# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------   
# Author:  chenhao
# Date:  2020-08-30
# Description:
#-------------------------------------------------------------------------------
import asyncio
import time
from random import randint

@asyncio.coroutine
def startState():
    print("start state called ")
    input_value = randint(0, 1)
    time.sleep(1)
    if input_value == 0:
        result = yield from State2(input_value)
    else:
        result = yield from State1(input_value)
    print("￥￥￥￥￥￥￥"+result)
    print("000start state calling" + result)

@asyncio.coroutine
def State1(transition_value):
    outputValue = str("State 1 with transition value = %s" % transition_value)
    input_value = randint(0, 1)
    time.sleep(1)
    print("...Evaluating...")
    if input_value == 0:
        result = yield from State3(input_value)
    else:
        result = yield from State2(input_value)
    result = "111state 1 calling" + result
    print("1111111111" + result)
    return outputValue + str(result)

@asyncio.coroutine
def State2(trainsition_value):
    outputValue =  str("State 2 with transition value = %s" % trainsition_value)
    input_value = randint(0, 1)
    time.sleep(1)
    print("...Evaluating...")
    if input_value == 0:
        result = yield from State1(input_value)
    else:
        result = yield from State3(input_value)
    result = "222state 2 calling" + result
    print("22222222" + result)
    return outputValue+ str(result)


@asyncio.coroutine
def State3(trainsition_value):
    outputValue =  str("State 3 with transition value = %s " % trainsition_value)
    input_value = randint(0, 1)
    time.sleep(1)
    print("...Evaluating...")
    if input_value == 0:
        result = yield from State1(input_value)
    else:
        result = yield from EndState(input_value)
    result = "333state 3 calling" + result
    print("333333333"+result)
    return outputValue+ str(result)

@asyncio.coroutine
def EndState(trainsition_value):
    outputValue = str("end state with transition value = %s" % trainsition_value)
    print("stop compution......")
    return outputValue

if __name__ == "__main__":
    print("finite state machine sumulation with asyncio coroutine")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(startState())