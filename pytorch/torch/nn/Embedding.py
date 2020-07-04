# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------   
# Author:  chenhao
# Date:  2020/7/4
# Email:  chenhao6@360.cn
# Description:
#-------------------------------------------------------------------------------
import torch

import torch.nn as nn
a1 = torch.LongTensor([[0,1,2],
                      [0,1,2]])  #貌似只能LongTensor型的
print(a1)
embed = nn.Embedding(10, 3)
print(embed(a1))