# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------   
# Author:  chenhao
# Date:  2020/7/4
# Email:  chenhao6@360.cn
# Description:
#-------------------------------------------------------------------------------
import torch
import numpy as np
a1 = torch.randint(1,50, (3, 5))
print(a1)
a2 = a1.chunk(5, 1) #按照axis=1分割为5块
print(a2)