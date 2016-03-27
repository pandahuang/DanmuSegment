#-*- coding: utf-8 -*-
__author__ = 'panda'

import os
import codecs
import json

def CountAmounts(danmakulist, count = -1, CallByAll = True):
    UserNumDict = {}
    UserIDList = [danmaku.getUserID() for danmaku in danmakulist]
    for user in UserIDList:
        if UserNumDict.has_key(user):
            UserNumDict[user] = UserNumDict[user] + 1
        else:
            UserNumDict[user] = 1
    if CallByAll:
        return len(UserNumDict.keys())
    else :
        print 'The userAmounts of the file %d is %d'%(count, len(UserNumDict.keys()))

def CountUserWords(danmakulist, count = -1, CallByAll = True):
    UserNumDict = {}
    UserIDList = [danmaku.getUserID() for danmaku in danmakulist]
    for user in UserIDList:
        if UserNumDict.has_key(user):
            UserNumDict[user] = UserNumDict[user] + 1
        else:
            UserNumDict[user] = 1
    if CallByAll:
        return UserNumDict
    else:
        with codecs.open(os.path.join(os.path.abspath('.'), 'UserWordsOf' + str(count)), 'w', 'utf-8') as fopen:
            fopen.write(json.dumps(sorted(UserNumDict.iteritems(), key = lambda d:d[1], reverse=True), ensure_ascii=False))

def CountUserSeries(danmakulist, count = -1, CallByAll = True):
    UserNumDict = {}
    UserIDList = [danmaku.getUserID() for danmaku in danmakulist]
    for user in UserIDList:
        UserNumDict[user] = 1
    if CallByAll:
        return UserNumDict

def DanmakuStatistic(danmakulist):
    pass