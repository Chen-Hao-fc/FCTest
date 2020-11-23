# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------   
# Author:  chenhao
# Date:  2020-09-29
# Description:
#-------------------------------------------------------------------------------
import tensorflow as tf

def expand_tile(value, size):
    """Add a new axis of given size."""
    value = tf.convert_to_tensor(value, name='value') #[past_length, past_length+1,...,past_length+nsteps-1]
    ndims = value.shape.ndims #value的长度？？ 返回value有几个维度
    print(ndims)
    return tf.tile(tf.expand_dims(value, axis=0), [size] + [1]*ndims)

with tf.Graph().as_default():
    # a = tf.constant([[0,1,2],[3,4,5]],name='a')
    # b = tf.tile(a,[2,3])
    # c = tf.shape(a)
    # d = tf.tile(a,[2]+[1]*1)
    # sess = tf.Session()
    # print(sess.run(b))
    # print(sess.run(c))
    # print(sess.run(d))
    # value = [2,3,4,5]
    # a1 = tf.convert_to_tensor(value, name='value')
    # # a2 = a1.shape.ndims
    # size = 4
    # c = expand_tile(value, size)
    # sess = tf.Session()
    # a1,  c = sess.run([a1,c])
    # print(a1)
    # print(c)
    # a = tf.range(3)
    # # b = a[:,None]
    # b = a-1
    # sess = tf.Session()
    # c, d = sess.run([a,b])

    i = tf.range(3)[:,None] #i的含义是输入每个词相对输入起始词的距离
    j = tf.range(8)
    m = i >= j - 8 + 3 #j−ns+nd=j−(ns−nd) (ns-nd)的意义是去除输入的上文长度,只剩下past的长度
    sess = tf.Session()
    c, d , e= sess.run([i,j,m])
    print(c)
    print(d)
    print(e)