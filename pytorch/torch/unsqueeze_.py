# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------   
# Author:  chenhao
# Date:  2020-08-10
# Description:
#-------------------------------------------------------------------------------
import torch
s1 = torch.arange(6).view((2,3))
print(s1)
print('---------')
print(s1.unsqueeze(0))
print(s1.squeeze(0))