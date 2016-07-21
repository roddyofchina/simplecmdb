#_*_coding:utf-8_*_
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group as SysGroup


class Department(models.Model):
    name = models.CharField(max_length=64,unique=True)
    def __unicode__(self):
        return self.name

    class Meta:
        permissions = (
            ("cmdb_dept_add", "添加部门信息"),
            ("cmdb_dept_view", "查看部门信息"),
            ("cmdb_dept_change", "修改部门信息"),
            ("cmdb_dept_delete", "删除部门信息"),
        )


class User(AbstractUser):
    #真实名字
    realname = models.CharField(max_length=20,null=True,default="admin")
    #电话号码
    phone = models.CharField(max_length=12,null=True)
    #部门
    department = models.ForeignKey('Department',null=True,)

    #用户头像
    photo = models.ImageField(upload_to='photos/' ,blank=True,null=True,default='/photos/userphoto.jpg')
    #用户QQ信息
    QQ = models.CharField(max_length=50,null=True,)

    def __unicode__(self):
        return self.realname

    class Meta:
        permissions = (
            ("cmdb_users_add", "添加用户"),
            ("cmdb_users_view", "查看用户"),
            ("cmdb_users_view_info", "查看用户详细"),
            ("cmdb_users_change", "修改用户"),
            ("cmdb_users_delete", "删除用户"),
            ("cmdb_users_restpass", "修改用户密码"),
        )

class History_Login(models.Model):
    user = models.ForeignKey(User)
    login_time = models.DateTimeField(auto_now_add=True)
    logout_time = models.DateTimeField(auto_now=True)
    user_ip = models.GenericIPAddressField()

    class Meta:
        permissions = (
            ("cmdb_history_view", "查看登录历史"),
            ("cmdb_history_delete", "删除登录历史"),
        )



