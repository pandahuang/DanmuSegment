#-*- coding: UTF-8 -*-
__author__ = 'panda'

import jieba.posseg as wflag
import danmaku
import os

def readDanmu(filename):
    danmulist = []
    fopen = open(filename)
    lines = fopen.readlines()
    for line in lines:
        danmu = line.strip('\n').strip('<d p="').strip('</d>')
        danmulist.append(danmu)
    return danmulist

def wordSegement(danmulist):
    danmakulist = []
    for danmu in danmulist:
        propertie_danmu = danmu.split('">')
        if len(propertie_danmu) == 2:
            properties = propertie_danmu[0].split(',')
            sentence = propertie_danmu[1]
            cutlist = wflag.cut(sentence)
            danmakuJ = danmaku.Danmaku()
            danmakuJ.setTime(properties[0])
            danmakuJ.setUserID(properties[6])
            danmakuJ.setDanmuID(properties[7])
            for word, flag in cutlist:
                danmakuJ.setWord(word, flag)
            danmakulist.append(danmakuJ)
    return danmakulist

# def wordFlag():
#     pass

def formatTrans():
    pass

def writeDanmaku():
    pass

if __name__ == '__main__':
    danmulists = readDanmu('D:\\python_workspace\\TSCwordSegmentation\\tsc\\example\\jieba\\FateUBW\\FateUBW00.xml')
    danmakulists = wordSegement(danmulists)
    print(len(danmulists))
    pass