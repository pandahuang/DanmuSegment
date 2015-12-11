#-*- coding: UTF-8 -*-
__author__ = 'panda'

import jieba.posseg as wflag
import danmaku
import json
import codecs
import os

def readDanmu(filename):
    danmulist = []
    fopen = codecs.open(filename, 'r', 'utf-8')
    lines = fopen.readlines()
    for line in lines:
        danmu = line.strip('\n').strip(u'<d p="').strip('\r')
        danmu = danmu.strip(u'</d>')
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
            # for word, flag in cutlist:
                # danmakuJ.setWord(word, flag)
            danmakuJ.WordFlag = cutlist
            danmakulist.append(danmakuJ)
    return danmakulist

def jsonformatTrans(danmakulist):
    jsonlist = []
    for danmaku in danmakulist:
        wf = {}
        wordproperties = {}
        wordproperties['danmu_ID'] = danmaku.getDanmuID()
        wordproperties['user_ID'] = danmaku.getUserID()
        wordproperties['Time'] = danmaku.getTime()
        for w, f in danmaku.WordFlag:
            key = w + '/' + f
            if wf.has_key(key): wf[key] = wf[key] + 1
            else: wf[key] = 1
        wordproperties['Word'] = wf
        jsonstr = json.dumps(wordproperties, ensure_ascii=False)
        jsonlist.append(jsonstr)
    return jsonlist

def writeDanmaku(jsonlist, filename):
    fwrite = codecs.open(filename, 'w', 'utf-8')
    for jsonstr in jsonlist:
        fwrite.write(jsonstr + '\n')
    fwrite.close()
    pass

def getFilelist(path = 'D:\\python_workspace\\TSCwordSegmentation\\tsc\\example\\jieba\\FateUBW'):
    filenamelist = []
    filelist = os.listdir(path)
    for file in filelist:
        filenamelist.append(path + '\\' + file)
    return filenamelist

def setFileName(path):
    filename = path + '.parse'
    return filename

if __name__ == '__main__':
    filenamelist = getFilelist()
    for filename in filenamelist:
        danmulists = readDanmu(filename)
        danmakulists = wordSegement(danmulists)
        print(len(danmakulists))
        writeDanmaku(jsonformatTrans(danmakulists), setFileName(filename))
    pass