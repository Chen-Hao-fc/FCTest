# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------   
# Author:  chenhao
# Date:  2020/7/4
# Description:
#-------------------------------------------------------------------------------
import torch

import torch.nn as nn
a1 = torch.LongTensor([[0,1,2],
                      [0,1,2]])  #貌似只能LongTensor型的
print(a1)
embed = nn.Embedding(10, 3)
print(embed(a1))
#sum函数测试

a2 = embed(torch.LongTensor([1,0]))
a3 = embed(torch.LongTensor([1,0]))
print(a2)
print(a2.size())
print('----')
print(a2.sum(0))
print(a3.sum(0))
print('----')
print(a2.sum(0)+a3.sum(0))