#-*- coding: utf-8 -*-
__author__ = 'panda'
import SingleAnalysis
import os
import codecs
import json

def UserSeriesNum(AllDanmaku):
    userSeries = {}
    for danmakulist in AllDanmaku: userSeries = dict(userSeries, **SingleAnalysis.userNumStatistics(danmakulist, ask = 'userPresents'))
    with codecs.open(os.path.join(os.path.abspath('.'), 'userSeries'), 'w', 'utf-8') as fopen:
        fopen.write(json.dumps(sorted(userSeries.iteritems(), key = lambda d:d[1], reverse=True), ensure_ascii=False))

