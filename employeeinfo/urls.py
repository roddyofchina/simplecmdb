
from django.conf.urls import patterns, include, url
from employeeinfo.views import *

urlpatterns = patterns('',
                       url(r'users/(\d+)$', employee_list, name='employee_list'),
                       url(r'users_query/$', users_query, name='users_query'),
                       url(r'emp/add/$', employee_add, name='employee_add'),
                       url(r'emp/del/(\d+)$', employee_del, name='employee_del'),
                       url(r'emp/detail/(\d+)$', employee_detail, name='employee_detail'),
                       url(r'emp/edit/(\d+)$', employee_edit, name='employee_edit'),
                       url(r'jobtitle/list/$', JobTitleList, name='jobtitle_list'),
                       url(r'jobtitle/add/$', JobTitleAdd, name='jobtitle_add'),
                       url(r'jobtitle/edit/(\d+)$', JobTitleEdit, name='jobtitle_edit'),
                       url(r'jobtitle/del/(\d+)$', JobTitleDel, name='jobtitle_del'),
)
