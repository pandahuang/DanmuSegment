#-*- coding: utf-8 -*-
__author__ = 'panda'

import danmaku
import tscSegment
import tsc.tscAnalysis.AllAnalysis
import tsc.tscAnalysis.SingleAnalysis
import os

'''Global Variable
'''
path = 'D:\\python_workspace\\TSCwordSegmentation\\tsc\\example\\jieba\\FateUBW'

if __name__ == '__main__':
    AllDanmaku, count = [], 0
    filenamelist = tscSegment.getFilelist(path)
    '''cut words
    '''
    for filename in filenamelist:
        danmulists = tscSegment.readDanmu(filename)
        danmakulists = tscSegment.wordSegement(danmulists)
        AllDanmaku.append(danmakulists)
        # dirname = tscSegment.setDirName(path, count)
        jsonlist = tscSegment.jsonformatTrans(danmakulists)
        '''AnalysisSingle
        '''
        tsc.tscAnalysis.SingleAnalysis.CountAmounts(danmakulists, count, CallByAll=False)
        tsc.tscAnalysis.SingleAnalysis.CountUserWords(danmakulists, count, CallByAll=False)
        count = count + 1
        print(len(danmakulists))
    '''AnalysisAll
    '''
    # tsc.tscAnalysis.AllAnalysis.DanmakuStatistics(AllDanmaku)

    pass