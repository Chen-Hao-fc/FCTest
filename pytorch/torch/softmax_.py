# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------   
# Author:  chenhao
# Date:  2020-09-13
# Description:
#-------------------------------------------------------------------------------
import torch
import torch.autograd as autograd
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
from torch.nn import Softmax

data=autograd.Variable(torch.FloatTensor([1.0,2.0,3.0]))
log_softmax=F.log_softmax(data,dim=0)
print(log_softmax)

softmax=F.softmax(data,dim=0)
print(softmax)

np_softmax=softmax.data.numpy()
log_np_softmax=np.log(np_softmax)
print(log_np_softmax)