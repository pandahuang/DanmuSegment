#-*- coding: UTF-8 -*-
__author__ = 'panda'

import jieba

cut_str = '同济大学软件学院23333336666卧槽'
cut_list =  jieba.cut(cut_str)
print "\t".join(cut_list)

import jieba.posseg as wflag

cut_list = wflag.cut(cut_str)
for word,flag in cut_list:
    print "\t" + word + "," + flag