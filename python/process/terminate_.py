# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------   
# Author:  chenhao
# Date:  2020-08-23
# Description:
#-------------------------------------------------------------------------------
import multiprocessing
import time

def foo():
    print('starting function')
    time.sleep(0.1)
    print('finished function')

if __name__ == '__main__':
    p = multiprocessing.Process(target=foo)
    print('Process before execution:', p, p.is_alive())
    p.start()
    print('Process running:', p, p.is_alive())
    p.terminate()
    # time.sleep(1)#这里都terminate了为啥还是true，这是因为系统停止一个进程需要时间，sleep 1秒后就变为false
    print('Process terminated:', p, p.is_alive())
    p.join()
    print('Process joined:', p, p.is_alive())
    print('Process exit code:', p.exitcode)
