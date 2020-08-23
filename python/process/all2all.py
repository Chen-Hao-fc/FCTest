# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------   
# Author:  chenhao
# Date:  2020-08-24
# Description:将scatter和gather集成到一起，all 到 all,也是就说每个进程都收集其他进程数据，也send数据给其他进程
#-------------------------------------------------------------------------------
from mpi4py import MPI
import numpy
com = MPI.COMM_WORLD
size = com.Get_size()
rank = com.Get_rank()
# print(size)
# senddata = numpy.array([rank*i for i in range(size)])
senddata = (rank+1)*numpy.arange(size,dtype=int)
# senddata = [rank*i for i in range(size)]

recvdata = numpy.empty(size,dtype=int)
#TODO 这里的send数据和rev数据都必须被numpy包装下，网上查了叫做什么buffer,可缓存的，用一般的list是不行的

# recvdata = xrange(size)
# recvdata = numpy.array(range(size))
#
com.Alltoall(senddata, recvdata)
print(" process %s sending %s receiving %s" % (rank , senddata , recvdata))
