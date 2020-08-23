# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------   
# Author:  chenhao
# Date:  2020-08-10
# Description:
#-------------------------------------------------------------------------------
import torch
# ss = torch.matmul()
s1 = torch.arange(6).view((2,3))
s2 = torch.arange(2).view((2,1))
print(s1)
print('---')
print(s2)
s3 = s1* s2
print(s3)
print(s3.size())
# s4 = s3.sum(dim=-1)
# print(s4)
# print(s4.size())
