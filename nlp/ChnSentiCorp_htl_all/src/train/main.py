# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------   
# Author:  chenhao
# Date:  2020-09-13
# Description:
#-------------------------------------------------------------------------------
import torch
import torch.nn as nn
from datetime import datetime
from absl import flags, app
from model import textcnn
import time
import numpy as np
from data.data_loader import ChnSentiCorpDataLoader

def parse_flags():
    #param
    flags.DEFINE_integer('epoch', 10, '')
    flags.DEFINE_string('device', 'cuda', '')
    flags.DEFINE_string('ckp','./../../data/checkpoint/','')
    flags.DEFINE_string('test_input', './../../data/prepro', '')
    #dataset
    flags.DEFINE_integer('batch_size', 64, 'batch size used in training')
    flags.DEFINE_boolean('shuffle', False, 'xxxxx')
    flags.DEFINE_string('input', './../../data/prepro', '')
    flags.DEFINE_integer('max_seq_len', 16, '')

    #model
    flags.DEFINE_integer('vocab_size', 28901, '')
    flags.DEFINE_integer('kernel_num', 5, '')
    flags.DEFINE_list('kernel_size', [4, 3, 2], '')
    flags.DEFINE_integer('embedding_dim', 256, '')
    flags.DEFINE_integer('class_num', 2, '')
    flags.DEFINE_float('dropout', 0.5, '')

    #optimizer
    flags.DEFINE_float('lr', 0.001, '')

    return flags.FLAGS


def main(args):
    start = datetime.now()
    FLAGS = parse_flags()
    model = textcnn.textcnn(FLAGS).to(FLAGS.device)
    print(model)
    optimizer = torch.optim.Adam(model.parameters(), lr=FLAGS.lr)
    criterion = nn.NLLLoss() #为了和log_softmax做配合

    data_loader = ChnSentiCorpDataLoader(param=FLAGS)
    curloss = np.inf
    for epoch in range(FLAGS.epoch):
        for idx, batch in enumerate(data_loader):
            label, sentence = batch
            out = model(sentence.type(torch.LongTensor).to(FLAGS.device))
            clas = label.type(torch.LongTensor).to(FLAGS.device)
            # print(out)
            loss = criterion(out, clas)
            loss.backward()
            optimizer.step()
            if (idx + 1) % 10 == 0:
                print("epoch:", epoch + 1, "step:", idx + 1, "loss:", loss.item())
            if loss < curloss:
                torch.save(model, FLAGS.ckp + '{}_model_epoch_{}_step_{}_loss_{:.2f}.pkl'.format(
                    time.strftime('%y%m%d%H%m%s'), epoch + 1, idx + 1, loss.item()))
                curloss = loss


    print('exec time is: %ss' % str((datetime.now() -start).seconds))


if __name__ == '__main__':
    app.run(main)





