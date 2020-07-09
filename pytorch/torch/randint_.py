# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------   
# Author:  chenhao
# Date:  2020/7/6
# Email:  chenhao6@360.cn
# Description:
#-------------------------------------------------------------------------------
import torch
a = torch.randint(0, 5, (3,4))  #在range(0,5)范围取随机数，然后view为(3,4)
print(a)
b = torch.randint(0, 5, (1,))
print(b)