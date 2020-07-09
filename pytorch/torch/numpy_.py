# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------   
# Author:  chenhao
# Date:  2020/7/4
# Email:  chenhao6@360.cn
# Description:
#-------------------------------------------------------------------------------
import torch
import numpy as np
s1 = np.array(range(9)).reshape(3, 3)
print(s1)
print('---------------')

s2 = torch.from_numpy(s1) #numpy -> tensor
print(s2)
print('---------------')

s3 = s2.numpy() #tensor -> numpy
print(s3)