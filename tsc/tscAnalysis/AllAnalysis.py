#-*- coding: utf-8 -*-
__author__ = 'panda'
import SingleAnalysis
import os
import codecs
import json
from collections import Counter
import tsc.tscSegement.tscSegment

def DanmakuStatistics(AllDanmaku):
    userAmounts = 0
    for danmakulist in AllDanmaku: userAmounts = userAmounts + SingleAnalysis.CountAmounts(danmakulist)
    print 'UserAmounts in all file is %d.'%userAmounts
    userSeries = {}
    for danmakulist in AllDanmaku: userSeries = dict(Counter(userSeries) + Counter(SingleAnalysis.CountUserSeries(danmakulist)))
    with codecs.open(os.path.join(os.path.abspath('.'), 'userSeries'), 'w', 'utf-8') as fopen:
        fopen.write(json.dumps(sorted(userSeries.iteritems(), key = lambda d:d[1], reverse=True), ensure_ascii=False))
    userWords = {}
    for danmakulist in AllDanmaku: userWords = dict(Counter(userWords) + Counter(SingleAnalysis.CountUserWords(danmakulist)))
    with codecs.open(os.path.join(os.path.abspath('.'), 'userWords'), 'w', 'utf-8') as fopen:
        fopen.write(json.dumps(sorted(userWords.iteritems(), key = lambda d:d[1], reverse=True), ensure_ascii=False))
