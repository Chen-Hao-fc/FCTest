# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------   
# Author:  chenhao
# Date:  2020-09-14
# Description:
#-------------------------------------------------------------------------------
import torch
import numpy as np
import os
from train.main import parse_flags
from absl import app

def main(args):
    FLAGS = parse_flags()
    path = os.path.join(FLAGS.ckp, os.listdir(FLAGS.ckp)[-1])
    model = torch.load(path).to(FLAGS.device)
    # print(model)
    test_data = open(FLAGS.input, 'r', encoding='utf-8').read().split('\n')[:100]
    seq_len = FLAGS.max_seq_len
    for data in test_data:
        tmp = data.split(',')
        label = int(tmp[0])
        txt = [int(token) for token in tmp[1].strip().split(' ')]
        # print(txt)
        if len(txt) >= seq_len:
            txt = txt[:seq_len]
        else:
            txt = txt + [0]*(seq_len-len(txt))
        sentence = np.array(txt)
        sentence = torch.from_numpy(sentence).unsqueeze(0).type(torch.LongTensor).to(FLAGS.device)
        clas = model(sentence).cpu().detach().numpy()[0]
        # print(clas)
        score = max(clas)
        clas = np.where(clas==score)[0][0]
        print(label==clas)

if __name__ == "__main__":
    app.run(main)