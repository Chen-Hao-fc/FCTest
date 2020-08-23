# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------   
# Author:  chenhao
# Date:  2020-08-23
# Description: 将不同数组中不同元素分发给process,
#发布的数据个数和process的个数相同
#-------------------------------------------------------------------------------
from mpi4py import MPI
com = MPI.COMM_WORLD
rank = com.rank

if rank == 0:
    array = range(10)
else:
    array = None

revive = com.scatter(array, root=0)
print('cur rank is:', rank, 'and recived data is:', revive)

