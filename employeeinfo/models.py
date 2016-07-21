#_*_coding:utf-8_*_
from django.db import models
from useraccount.models import Department


'''职位管理表'''
class jobtitle(models.Model):
    name = models.CharField(max_length=128, blank=True, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        permissions = (
            ("cmdb_jobtitle_add", "添加职位"),
            ("cmdb_jobtitle_view", "查看职位"),
            ("cmdb_jobtitle_change", "修改职位"),
            ("cmdb_jobtitle_delete", "删除职位"),
        )


'''员工管理表'''
class Employee(models.Model):
    name = models.CharField(max_length=128, blank=True, unique=True)
    number = models.IntegerField(u'员工编号', null=True,blank=True,unique=True)
    sex_status = (
        (1,'男'),
        (2,'女'),
    )
    sex = models.SmallIntegerField(u'姓别', choices= sex_status,null=True,blank=True)
    contact = models.CharField(max_length=128, null=True)
    jobtitle = models.ForeignKey('jobtitle')
    email = models.CharField(max_length=128, blank=True,  null=True)
    dept = models.ForeignKey(Department, null=True)
    u_status = (
        (1, '在职'),
        (2, '离职'),
    )
    age = models.SmallIntegerField(u'年龄', null=True)
    status = models.SmallIntegerField(u'状态', choices=u_status,null=True, blank=True)
    birthday = models.CharField(max_length=128, blank=True, null=True)
    universit = models.CharField(max_length=128, blank=True, null=True)
    EntryTime = models.CharField(u'入职时间', max_length=128, null=True)
    ExitTime = models.CharField(u'离职时间', max_length=128, null=True)
    family_address = models.CharField(max_length=255, blank=True,  null=True)
    description = models.CharField(max_length=255, blank=True,  null=True)

    #员工照片
    photo = models.ImageField(upload_to='photos/', blank=True, null=True,)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "employee"
        permissions = (
            ("cmdb_employee_add", "添加员工信息"),
            ("cmdb_employee_view", "查看员工信息"),
            ("cmdb_employee_change", "修改员工信息"),
            ("cmdb_employee_delete", "删除员工信息"),
        )