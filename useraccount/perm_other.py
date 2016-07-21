#!/usr/bin/env python
#coding:utf-8

__author__ = 'Luodi'

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

def addpermission():
    countid=Permission.objects.filter(codename__contains="cmdb_group").count()
    if countid == 0:
        content_type = ContentType.objects.get(app_label='auth', model='Group')
        Permission.objects.create(codename='cmdb_group_add',name='添加用户组',content_type=content_type)
        Permission.objects.create(codename='cmdb_group_delete',name='删除用户组',content_type=content_type)
        Permission.objects.create(codename='cmdb_group_view',name='查看用户组',content_type=content_type)
        Permission.objects.create(codename='cmdb_group_change',name='修改用户组',content_type=content_type)

    pcountid=Permission.objects.filter(codename__contains="cmdb_permission").count()
    if pcountid == 0:
        content_type = ContentType.objects.get(app_label='auth', model='Permission')
        Permission.objects.create(codename='cmdb_permission_view',name='查看组权限',content_type=content_type)
        Permission.objects.create(codename='cmdb_permission_change',name='修改组权限',content_type=content_type)


