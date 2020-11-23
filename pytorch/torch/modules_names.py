# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------   
# Author:  chenhao
# Date:  2020-10-02
# Description:
#-------------------------------------------------------------------------------
import torch.nn as nn
import torch.nn.functional as F

class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.conv1xxxx = nn.Conv2d(1, 20, 5)
        self.conv2 = nn.Conv2d(20, 20, 5)
        # conv3 = nn.Conv2d(20, 20, 6)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        return F.relu(self.conv2(x))
print('hello world')
net = Model()
# print(net.named_parameters())
for idx, m in enumerate(net.named_modules()):
    print(idx, '->', m)
# for param in net.parameters():
#     print(type(param), param.size())
print('-'*100)
for idx, m in enumerate(net.named_children()):
    print(idx, '->', m)