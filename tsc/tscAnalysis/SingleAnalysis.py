#-*- coding: utf-8 -*-
__author__ = 'panda'

def userNumStatistics(danmukulist, ask):
    TimeList = [danmaku.Time for danmaku in danmukulist]
    UserIDList = [danmaku.user_ID for danmaku in danmukulist]
    return Count(UserIDList, ask)
    pass

def Count(UserIDList, ask = 'userAmounts'):
    UserNumDict = {}
    for user in UserIDList:
        # if UserNumDict.has_key(user):
        #     UserNumDict[user] = UserNumDict[user] + 1
        # else:
        UserNumDict[user] = 1
    if ask == 'userAmounts':
        return len(UserNumDict.keys())
    if ask == 'userWords':
        return sorted(UserNumDict.iteritems(), key = lambda d:d[1], reverse=True).keys()
    if ask == 'userPresents':
        return UserNumDict
