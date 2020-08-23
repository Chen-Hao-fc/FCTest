# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------   
# Author:  chenhao
# Date:  2020-08-23
# Description:
#-------------------------------------------------------------------------------
from mpi4py import MPI
com = MPI.COMM_WORLD
rank = com.rank
print('my rank in:', rank)
import time

# if rank == 1:
#     data_send = 'a'
#     destination_process = 5
#     recv_prpcess = 5
#     com.send(data_send, dest=destination_process)
#     time.sleep(10)
#     data_received = com.recv(source=recv_prpcess)
#     # com.send(data_send, dest=destination_process)
#     print("sending data %s " %data_send + "to process %d" %destination_process)
#     print("data received is = %s" %data_received)
#
#
# if rank == 5:
#     data_send = 'b'
#     destination_process = 1
#     recv_prpcess = 1
#     data_received = com.recv(source=recv_prpcess)
#     time.sleep(10)
#     com.send(data_send, dest=destination_process)
#     print("sending data %s " %data_send + "to process %d" %destination_process)
#     print("data received is = %s" %data_received)


if rank==1:
    data_send= "a"
    destination_process = 5
    source_process = 5
    data_received=com.sendrecv(data_send,dest=destination_process,source =source_process)
if rank==5:
    data_send= "b"
    destination_process = 1
    source_process = 1
    data_received=com.sendrecv(data_send,dest=destination_process, source=source_process)