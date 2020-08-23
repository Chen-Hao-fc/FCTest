# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------   
# Author:  chenhao
# Date:  2020-08-23
# Description: 将一个元素分发给所有的process
#-------------------------------------------------------------------------------
from mpi4py import MPI
import time
com = MPI.COMM_WORLD
rank = com.Get_rank()

# print('my rank is:', rank)
if rank == 0:
    shared = 'a'
else:
    shared = None

var_shared = com.bcast(shared, root=0)
# time.sleep(3)
print('prcess is :', rank, 'shared is:', var_shared)



