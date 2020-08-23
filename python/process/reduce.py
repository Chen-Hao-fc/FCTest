# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------   
# Author:  chenhao
# Date:  2020-08-24
# Description: 简化版的gather 操作
#-------------------------------------------------------------------------------
import numpy as np

from mpi4py import MPI
com = MPI.COMM_WORLD
size = com.Get_size()
rank = com.Get_rank()
recvdata = np.zeros(size,dtype=np.int)
senddata = np.array([rank*i for i in range(size)],dtype=np.int)
print("process %s sending %s " % (rank , senddata))
com.Reduce(senddata, recvdata, root=0, op=MPI.SUM)
print('on task', rank, 'after Reduce:    data = ', recvdata)