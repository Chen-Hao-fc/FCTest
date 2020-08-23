# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------   
# Author:  chenhao
# Date:  2020-08-24
# Description: 一个进程收集所有进行的数据
#-------------------------------------------------------------------------------
from mpi4py import  MPI
com = MPI.COMM_WORLD
size = com.Get_size()
rank  = com.Get_rank()
data = rank*2
data2 = com.gather(data, root=0)
if rank==0:
    print('rank=',rank, '...recieve data to other process')
    for i in range(0, size):
        # data[i] = (i+1)**2
        value = data2[i]
        print(" process %s receiving %s from process %s" % (rank , value , i))

