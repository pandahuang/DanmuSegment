#-*- coding: UTF-8 -*-
__author__ = 'panda'

import jieba.posseg as wflag
import danmaku
import json
import codecs
import os

def readDanmu(filename):
    danmulist = []
    with codecs.open(filename, 'r', 'utf-8') as fopen:
        for line in fopen.readlines():
            danmu = line.strip('\n').strip(u'<d p="').strip('\r')
            danmu = danmu.strip(u'</d>')
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
            danmakuJ.WordFlag = cutlist
            danmakulist.append(danmakuJ)
    return danmakulist

def jsonformatTrans(danmakulist, dirname = ''):
    jsonlist = []
    for danmaku in danmakulist:
        wordproperties = jsonLtpConvertor(danmaku)
        jsonstr = json.dumps(wordproperties, ensure_ascii=False)
        writeDanmakuByDanmu(jsonstr, os.path.join(dirname, danmaku.getDanmuID() + '.parse'))
        jsonlist.append(jsonstr)
    return jsonlist

def jsonLtpConvertor(danmaku):
    words, pos = [], 0
    for w, f in danmaku.WordFlag:
        contents = {}
        contents['id'] = pos
        contents['cont'] = w
        contents['pos'] = f
        contents['semparent'] = '-1'
        contents['semrelate'] = 'None'
        pos = pos + 1
        words.append(contents)
    return words

def writeDanmakuByDanmu(jsonstr, filename):
    with codecs.open(filename, 'w', 'utf-8') as fwrite:
        fwrite.write(jsonstr)

def writeDanmaku(jsonlist, filename):
    fwrite = codecs.open(filename, 'w', 'utf-8')
    for jsonstr in jsonlist:
        fwrite.write(jsonstr + '\n')
    fwrite.close()
    pass

def getFilelist(path):
    filenamelist = []
    for file in os.listdir(path):
        filenamelist.append(path + '\\' + file)
    return filenamelist

def setDirName(path, count):
    dirstr = 'parse' + str(count)
    dirname = os.path.join(os.path.join(os.path.split(path)[0], 'parses'), dirstr)
    os.mkdir(dirname)
    print 'Writing dir : %s ...'%dirname
    return dirname
