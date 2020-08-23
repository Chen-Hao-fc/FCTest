# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------   
# Author:  chenhao
# Date:  2020-08-23
# Description:
#-------------------------------------------------------------------------------
from mpi4py import MPI
comm = MPI.COMM_WORLD
import time

rank = comm.rank
print('my rank is:', rank)
if rank == 0:
    data = 1000000
    destination_process = 4
    time.sleep(10)
    comm.send(data, dest=destination_process)
    print('sending data % s' % data + 'to process %d' % destination_process)
if rank == 1:
    destination_process = 8
    data = 'hello'
    time.sleep(10)
    comm.send(data, dest=destination_process)
    print('sending data % s' % data + 'to process %d' % destination_process)

if rank == 4:
    time.sleep(10)
    data = comm.recv(source=0)

    print('data received is = %s' % data)

if rank == 8:
    time.sleep(10)
    data = comm.recv(source=1)
    print('data received is = %s' % data)


