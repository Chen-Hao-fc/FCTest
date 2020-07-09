# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------   
# Author:  chenhao
# Date:  2020/7/4
# Email:  chenhao6@360.cn
# Description:底层存储的 tensor是否是连续的
#-------------------------------------------------------------------------------
import torch
import numpy as np
s1 = torch.arange(0, 9).view(3,3)
print(s1)
print('-----------------')

s2 = s1.t() #

print(s1.is_contiguous(), s2.is_contiguous()) #True, s1底层是按照顺序存储的   s2底层是指针指向s1,底层不是按照顺序存的
print('-----------------')
print(s1.flatten())  #tensor([0,   1,   2,   3,   4,   5,   6,   7,   8])
print(s2.flatten())  #tensor([0,   3,   6,   1,   4,   7,   2,   5,   8])
print('------------------')
s2 = s2.contiguous() #将s2底层数据转为顺序存储
print(s2.is_contiguous())


