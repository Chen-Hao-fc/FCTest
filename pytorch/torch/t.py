# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------   
# Author:  chenhao
# Date:  2020/7/4
# Email:  chenhao6@360.cn
# Description: tensor转置(必须是二维tensor以上)
#-------------------------------------------------------------------------------
import torch
s1 = torch.arange(0,9).view(3,3)
print(s1)
print('---------------')
print(s1.t())