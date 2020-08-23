# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------   
# Author:  chenhao
# Date:  2020-08-23
# Description:
#-------------------------------------------------------------------------------
import multiprocessing
from mpi4py import MPI
def function_square(item):
    return item * item

if __name__ == '__main__':
    inputs = range(100)
    pool = multiprocessing.Pool(processes=4)

    outputs = pool.map(function_square, inputs)

    pool.close()
    pool.join()

    print(outputs)