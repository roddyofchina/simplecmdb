from django.conf.urls import patterns, include, url
from useraccount.views import *

urlpatterns = patterns('',
                       url(r'login/$', login_user, name='login_user'),
                       url(r'^logout/$', logout_user, name='logout_user'),
                       url(r'^list/(\d+)$', users_list, name='users_list'),
                       url(r'^info/(\d+)$', users_info, name='users_info'),
                       url(r'^add/$', users_add, name='users_add'),
                       url(r'^edit/(\d+)$', users_update, name='users_update'),
                       url(r'^del/(\d+)$', users_del, name='users_del'),
                       url(r'^history/(\d+)$', users_history, name='users_history'),
                       url(r'^del_history/(\d+)$', users_history_del, name='users_history_del'),
                       url(r'^setpasswd/(\d+)$',userset_password, name='userset_password'),


                       url(r'^groups/list/(\d+)$', users_group_list, name='users_group_list'),
                       url(r'^groups/del/(\d+)$', users_group_del, name='users_group_del'),
                       url(r'^groups/add/$', users_group_add,name='users_group_add'),
                       url(r'^groups/edit/(\d+)$', users_group_edit, name='users_group_edit'),
                       url(r'^groups/manager/(\d+)$', users_group_manager, name='users_group_manager'),


                       url(r'^permissions/list/(\d+)$', User_permissions, name='User_permissions'),
                       url(r'^permissions/manager/(\d+)$', users_permission_managers, name='users_permission_managers'),

                       url(r'^dept/list/(\d+)$', dept_lists, name='dept_lists'),
                       url(r'^dept/del/(\d+)$', dept_del, name='dept_del'),
                       url(r'^dept/add/$', dept_add, name='dept_add'),
                       url(r'^dept/edit/(\d+)$', dept_edit, name='dept_edit'),

)