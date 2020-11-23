# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------   
# Author:  chenhao
# Date:  2020-09-13
# Description:
#-------------------------------------------------------------------------------
import torch
import torch.nn as nn
from torch.nn import functional as F

class textcnn(nn.Module):
    def __init__(self, param):
        # super(textcnn, self).__init__()
        super().__init__()
        vocab_size = param.vocab_size
        kernel_num = param.kernel_num
        kernel_size = param.kernel_size
        embedding_dim = param.embedding_dim
        class_num = param.class_num
        dropout = param.dropout

        self.embed = nn.Embedding(vocab_size, embedding_dim, padding_idx=1)
        self.conv0 = nn.Conv2d(1, kernel_num, (kernel_size[0], embedding_dim))
        self.conv1 = nn.Conv2d(1, kernel_num, (kernel_size[1], embedding_dim))
        self.conv2 = nn.Conv2d(1, kernel_num, (kernel_size[2], embedding_dim))

        self.dropout = nn.Dropout(dropout)

        self.line = nn.Linear(len(kernel_size)*kernel_num, class_num)

    @classmethod
    def from_dict(cls, obj_dict, **kwargs):
        return cls(**obj_dict, **kwargs)

    @staticmethod
    def conv_and_pool(x, conv):
        # x: (batch, 1, sentence_length,  )
        x = conv(x)
        # x: (batch, kernel_num, H_out, 1)
        x = F.relu(x.squeeze(3))
        # x: (batch, kernel_num, H_out)
        x = F.max_pool1d(x, x.size(2)).squeeze(2)
        #  (batch, kernel_num)
        return x

    def forward(self, x):
        x = self.embed(x)
        x = x.unsqueeze(1)
        out1 = self.conv_and_pool(x, self.conv0)
        out2 = self.conv_and_pool(x, self.conv1)
        out3 = self.conv_and_pool(x, self.conv2)
        x = torch.cat([out1, out2, out3], 1)
        x = self.dropout(x)
        x= self.line(x)
        # logit = F.softmax(x, dim=1)
        logit = F.log_softmax(x, dim=1)#这里由于最后用NLLLoss所以这里直接取log
        return logit



