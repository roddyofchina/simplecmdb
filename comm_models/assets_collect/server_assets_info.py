#!/usr/bin/env python
#coding:utf-8

__author__ = 'Luodi'

import urllib2,urllib

try:
    import json
except ImportError:
    import simplejson as json

class Get_Server_Assets(object):

    __token_id = ''
    def __init__(self,url,username,passwd):
        self.__url = url
        self.__user = username
        self.__password = passwd
        ''' user login and get token id '''
        params = {'eauth': 'pam', 'username': self.__user, 'password': self.__password}
        encode = urllib.urlencode(params)
        obj = urllib.unquote(encode)
        content = self.postRequest(obj, prefix='/login')
        try:
            self.__token_id = content['return'][0]['token']
        except KeyError:
            raise KeyError

    '''Salt URL请求'''
    def postRequest(self,obj,prefix='/'):
        url = self.__url + prefix
        headers = {'X-Auth-Token'   : self.__token_id}
        req = urllib2.Request(url, obj, headers)
        opener = urllib2.urlopen(req)
        content = json.loads(opener.read())
        return content

    def grains(self,tgt,arg):
        ''' 获取salt客户端服务器硬件信息 '''
        params = {'client': 'local', 'tgt': tgt, 'fun': 'grains.items', 'arg': arg}
        obj = urllib.urlencode(params)
        content = self.postRequest(obj)
        ret = content['return'][0]
        return ret

if __name__ == "__main__":
    SALT=Get_Server_Assets(url="http://123.56.79.112:8000",username='jenkins',passwd='LDjtjenkins2016')
    a=SALT.grains('*', '')
    for saltgrains in a:

        print saltgrains,a[saltgrains]['biosversion'],a[saltgrains]['kernelrelease'],a[saltgrains]['hwaddr_interfaces']



