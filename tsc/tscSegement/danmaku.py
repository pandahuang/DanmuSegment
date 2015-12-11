#-*- coding: UTF-8 -*-
__author__ = 'panda'

class Danmaku(object):
    danmu_ID = ''
    user_ID = ''
    # Word = {}
    Time = ''

    def __init__(self):
        pass

    def setDanmuID(self, danmu_id): self.danmu_ID = danmu_id

    def getDanmuID(self): return self.danmu_ID

    def setUserID(self, user_id): self.user_ID = user_id

    def getUserID(self): return self.user_ID

    # def setWord(self, content, flag):
    #     key = content + '/' + flag
    #     if self.Word.has_key(key):
    #         self.Word[key] = self.Word.get(key) + 1
    #     else:
    #         self.Word[key] = 1
    #
    # def getWord(self): return self.Word

    # def setFlag(self, flag): self.Flag = flag

    # def getFlag(self): return self.Flag

    def setTime(self, time): self.Time = time

    def getTime(self): return self.Time

    pass