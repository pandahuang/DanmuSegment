#-*- coding: UTF-8 -*-
__author__ = 'panda'

import jieba.posseg as wflag
import danmaku
import json
import os

def readDanmu(filename):
    danmulist = []
    fopen = open(filename)
    lines = fopen.readlines()
    for line in lines:
        danmu = line.strip('\n').strip('<d p="').strip('</d>')
        danmulist.append(danmu)
    fopen.close()
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

def jsonformatTrans(danmakulist):
    jsonlist = []
    for danmaku in danmakulist:
        jsondata = []
        wordproperties = {}
        wordproperties['danmu_ID'] = danmaku.getUserID()
        wordproperties['user_ID'] = danmaku.getUserID()
        wordproperties['Time'] = danmaku.getTime()
        wordproperties['Word'] = danmaku.getWord()
        jsonstr = json.dumps(wordproperties)
        jsonlist.append(jsonstr)
    return jsonlist

def writeDanmaku(jsonlist, filename):
    fwrite = open(filename, 'w')
    count = 1
    for jsonstr in jsonlist:
        while count == 1:
            fwrite.write(jsonstr + '\n')
            count = count + 1
    fwrite.close()
    pass

if __name__ == '__main__':
    danmulists = readDanmu('D:\\python_workspace\\TSCwordSegmentation\\tsc\\example\\jieba\\FateUBW\\FateUBW00.xml')
    danmakulists = wordSegement(danmulists)
    print(len(danmakulists))
    writeDanmaku(jsonformatTrans(danmakulists), 'D:\\python_workspace\\TSCwordSegmentation\\tsc\\example\\jieba\\FateUBW\\parses')
    pass