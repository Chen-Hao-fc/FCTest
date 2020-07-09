# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------   
# Author:  chenhao
# Date:  2020/7/6
# Email:  chenhao6@360.cn
# Description:
#-------------------------------------------------------------------------------
import torch

a = torch.arange(12).view(3,4)
print(a)
a = a.flatten()
print(a.view(4, -1))
