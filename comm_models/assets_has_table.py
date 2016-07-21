#!/usr/bin/env python
#coding:utf-8
__author__ = 'Luodi'


#判断资产关联的资源表
def tablehas(sdata,assetbales):
    for ctable in assetbales:
        if hasattr(sdata,ctable):
            return ctable
    else:
        return ""
