# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------   
# Author:  chenhao
# Date:  2020-09-12
# Description:
#-------------------------------------------------------------------------------
import jieba

def stopwords(path):
    return [w.strip() for w in open(path,'r',encoding='utf-8').read().split('\n')]


def loadRawData(path):
    labels, txts = [], []
    with open(path, 'r', encoding='utf-8') as fr:
        next(fr)
        line = fr.readline()
        while line:
            tmp = line.strip().split(',')
            if len(tmp)>=2:
                label, txt = tmp[0], jieba.cut(','.join(tmp[1:]), cut_all=False)
                # print(label)
                assert label in ['0', '1']
                labels.append(label)
                txts.append([w for w in txt])
            line = fr.readline()

    return labels, txts


def structVoc(txts, path, stopw):
    stopw = set(stopw)
    wordCount = {}
    vocabulary = {}
    for txt in txts:
        for token in txt:
            if token not in stopw:
                if token not in wordCount:
                    wordCount[token] = 1
                else:
                    wordCount[token] += 1

    # save vocabulary
    with open(path, 'w', encoding='utf-8') as fw:
        for ith, (key, value) in enumerate(sorted(wordCount.items(), key=lambda x: x[1], reverse=True)):
            vocabulary[key] = str(ith)
            fw.write(key +' '+ str(ith) +' '+ str(value) + '\n')

    return vocabulary


def main():
    rawP = './../../data/raw'
    stopwP = './../../data/stopwords'
    vocP = './../../data/vocabulary'
    output = './../../data/prepro'
    labels, txts = loadRawData(rawP)
    stopw = stopwords(stopwP)
    voc = structVoc(txts, vocP, stopw)
    print('the num for txt:', len(txts))
    print('the voc size is:', len(voc))

    with open(output, 'w', encoding='utf-8') as fw:
        for label, txt in zip(labels, txts):
            txt2idx = ' '.join([voc[token] for token in txt if token in voc])
            if len(txt2idx.strip()) > 0:
                fw.write(label + ',' + txt2idx + '\n')

if __name__ == '__main__':
    main()





