#!/usr/bin/env python
#coding:utf-8

__author__ = 'Luodi'

from django.conf.urls import patterns, include, url
from assetsinfo.views import *

urlpatterns = patterns('',
  url(r'^list/(\d+)$',assets_list,name='assets_list'),
  url(r'^del/(\d+)$',assets_del,name='assets_del'),
  url(r'^add/$',assets_add, name='assets_add'),
  url(r'^detail/(\d+)$', assets_details, name='assets_detail'),
  url(r'^edit/(\d+)$', assets_edit, name='assets_edit'),
  url(r'^idc/list/$', idc_list, name='idc_list'),
  url(r'^idc/delete/(\d+)$', idc_del, name='idc_del'),
  url(r'^idc/idcedit/(\d+)$', idc_edit, name='idc_edit'),
  url(r'^business/list/$', business_list, name='business_list'),
  url(r'^business/edit/(\d+)$', business_edit, name='business_edit'),
  url(r'^business/del/(\d+)$', business_del, name='business_del'),
  url(r'^devicetype/list/$', devicetype_list, name='devicetype_list'),
  url(r'^devicetype/edit/(\d+)$', devicetype_edit, name='devicetype_edit'),
  url(r'^devicetype/del/(\d+)$', devicetype_del, name='devicetype_del'),
  url(r'^provider/list/$', provider_list, name='provider_list'),
  url(r'^provider/del/(\d+)$', provider_del, name='provider_del'),
  url(r'^server/list/$', Assets_server_list, name='Assets_server_list'),
  url(r'^server/edit/(\d+)$', Assets_server_edit, name='Assets_server_edit'),
  url(r'^server/add/$', Assets_server_add, name='Assets_server_add'),
  url(r'^server/del/(\d+)$', Assets_server_del, name='Assets_server_del'),
)


