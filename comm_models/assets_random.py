#!/usr/bin/env python
#coding:utf-8

__author__ = 'Luodi'

import datetime
import random

def GetAssetsNum():
    for i in range (0,10):
        nowTime=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        randomNum=random.randint(0,100)
        if randomNum<=10:
            randomNum=str(0)+str(randomNum)
        uniqueNum=str(nowTime)+str(randomNum)
        AssetsNum = 'QX' + uniqueNum
        return AssetsNum
