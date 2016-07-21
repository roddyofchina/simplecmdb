#_*_coding:utf-8_*_
from django.db import models
from employeeinfo.models import Employee
from useraccount.models import User


'''设备类型表'''
class DeviceType(models.Model):
    name = models.CharField(max_length=128,blank=True,)

    def __unicode__(self):
        return self.name

    class Meta:       permissions = (
            ("cmdb_devicetype_add", "添加设备类型"),
            ("cmdb_devicetype_view", "查看设备类型"),
            ("cmdb_devicetype_change", "修改设备类型"),
            ("cmdb_devicetype_delete", "删除设备类型"),
        )



'''IDC信息管理表'''
class IDC(models.Model):
    idc_name = models.CharField(max_length=128, blank=True, unique=True)
    address = models.CharField(max_length=255, null=True,blank=True)
    floor = models.CharField(u'楼层',max_length=20,null=True,blank=True)
    contacts = models.CharField(max_length=128, null=True,blank=True)
    phone = models.CharField(max_length=20,null=True,blank=True)


    def __unicode__(self):
        return self.idc_name

    class Meta:
        permissions = (
            ("cmdb_idc_add", "添加IDC"),
            ("cmdb_idc_view", "查看IDC"),
            ("cmdb_idc_change", "修改IDC"),
            ("cmdb_idc_delete", "删除IDC"),
        )



'''业务表'''
class Business(models.Model):
    name = models.CharField(max_length=128, blank=True, unique=True)

    def __unicode__(self):
        return self.name


    class Meta:
        permissions = (
            ("cmdb_devicetype_add", "添加业务"),
            ("cmdb_devicetype_view", "查看业务"),
            ("cmdb_devicetype_change", "修改业务"),
            ("cmdb_devicetype_delete", "删除业务"),
        )



'''提供商表'''
class Provider(models.Model):
    provider_name = models.CharField(max_length=128, blank=True, unique=True)
    address = models.CharField(max_length=255, null=True)
    contacts = models.CharField(max_length=128, null=True)
    phone = models.CharField(max_length=20,null=True)
    Fax = models.CharField(max_length=20,null=True)

    def __unicode__(self):
        return self.provider_name

    class Meta:
        permissions = (
            ("cmdb_provider_add", "添加提供商"),
            ("cmdb_provider_view", "查看提供商"),
            ("cmdb_provider_change", "修改提供商"),
            ("cmdb_provider_delete", "删除提供商"),
        )



'''资产表'''
class Assets(models.Model):

    Assets_name = models.CharField(max_length=128, blank=True, unique=True)

    device_number = models.CharField(max_length=128, blank=True, unique=True)

    device_type = models.ForeignKey('DeviceType')

    #保修期
    Warranty = models.SmallIntegerField(u'保修期',null=True)

    IDC = models.ForeignKey('IDC',null=True, blank=True)

    #负责人
    principal = models.ForeignKey(Employee, related_name='principal_s',null=True, default=None)

    #使用人
    Employee = models.ForeignKey(Employee, related_name='Employee_set',null=True)

    business = models.ForeignKey('Business')

    buy_time = models.CharField(u'购买日期', max_length=128,null=True, blank=True)

    buy_type_choice = (
        (1, u'公司内购'),
        (2, u'员工自购'),
    )

    buy_type = models.SmallIntegerField(u'购买方式',choices=buy_type_choice,null=True,blank=True)

    price = models.IntegerField(u'购买价格', null=True,blank=True)


    #管理员,可以是多个管理员进行维护
    admin = models.ManyToManyField(User, blank=True)

    suse_time = models.CharField(u'开始使用时间', max_length=128, null=True)

    euse_time = models.CharField(u'截至使用时间', max_length=128, null=True)

    status_choice = (
        (1, u'正在使用'),
        (2, u'未使用'),
        (3, u'设备故障'),
        (4, u'库存备用'),
    )

    status =models.SmallIntegerField(u'状态',choices=status_choice,null=True,blank=True)

    create_time = models.DateTimeField(u'资产创建时间', auto_now_add=True,null=True)

    devicetag = models.CharField(max_length=255, blank=True, null=True)

    #提供商
    provider = models.ForeignKey('Provider')

    #其它备注
    description = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return self.Assets_name

    class Meta:
        permissions = (
            ("cmdb_assets_add", "添加资产"),
            ("cmdb_assets_view", "查看资产"),
            ("cmdb_assets_change", "修改资产"),
            ("cmdb_assets_delete", "删除资产"),
        )



'''软件版本'''
class Software(models.Model):
    name = models.CharField(max_length=128, blank=True)
    version = models.CharField(max_length=128,null=True, blank=True)
    license = models.CharField(max_length=128,null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        permissions = (
            ("cmdb_software_add", "添加软件"),
            ("cmdb_software_view", "查看软件"),
            ("cmdb_software_change", "修改软件"),
            ("cmdb_software_delete", "删除软件"),
        )





'''服务器主表'''
class Server(models.Model):
    Assets = models.OneToOneField('Assets')

    sninfo = models.CharField(max_length=128)

    #产商
    Firm = models.CharField(max_length=128,null=True, blank=True)

    #型号
    model = models.CharField(max_length=128,null=True,blank=True)

    #软件安装列表
    software  = models.ManyToManyField('Software', blank=True)

    #raid
    raid = models.CharField(max_length=128,null=True,blank=True)

    create_time = models.DateTimeField(blank=True, auto_now_add=True)

    #修改时间
    update_time = models.DateTimeField(blank=True, auto_now=True, null=True)

    def __unicode__(self):
        return self.sninfo

    class Meta:
        permissions = (
            ("cmdb_server_add", "添加服务器"),
            ("cmdb_server_view", "查看服务器"),
            ("cmdb_server_change", "修改服务器"),
            ("cmdb_server_delete", "删除服务器"),
        )




'''系统信息'''
class kernel_info(models.Model):
    platform = models.CharField(max_length=128,null=True, blank=True)

    system = models.CharField(max_length=128,null=True, blank=True)

    version = models.CharField(max_length=128,null=True, blank=True)

    create_time = models.DateTimeField(blank=True, auto_now_add=True)

    update_time = models.DateTimeField(blank=True, auto_now=True)

    server = models.ForeignKey('Server',null=True)


class Cpu(models.Model):
    #cpu架构
    Architecture = models.CharField(max_length=128,blank=True,null=True)
    #产商
    Vendor_id = models.CharField(max_length=128,blank=True,null=True)
    #型号
    model = models.CharField(max_length=128,blank=True,null=True)

    cpus = models.SmallIntegerField(null=True)

    cpu_mhz = models.CharField(max_length=128,blank=True,null=True)

    L1cache = models.CharField(max_length=128,blank=True,null=True)

    L2cache = models.CharField(max_length=128,blank=True,null=True)

    L3cache = models.CharField(max_length=128,blank=True,null=True)

    Thread = models.SmallIntegerField(null=True)

    create_time = models.DateTimeField(blank=True, auto_now_add=True)

    update_time = models.DateTimeField(blank=True, auto_now=True)

    tag = models.CharField(max_length=128,blank=True,null=True)

    server = models.ForeignKey('Server',null=True)






class Mem(models.Model):
    capacity = models.CharField(max_length=128,null=True, blank=True)

    swap = models.CharField(max_length=128,null=True, blank=True)

    number = models.CharField(max_length=128,null=True, blank=True)

    create_time = models.DateTimeField(blank=True, auto_now_add=True)

    update_time = models.DateTimeField(blank=True, auto_now=True)

    tag = models.CharField(max_length=128,blank=True,null=True)

    server = models.ForeignKey('Server',null=True)



'''硬盘信息表'''
class Disk(models.Model):
    name  = models.CharField(max_length=128,blank=True)

    sn = models.CharField(max_length=128,blank=True)
    #产商
    Firm = models.CharField(max_length=128,null=True, blank=True)
    #容量
    capacity = models.CharField(max_length=128,null=True, blank=True)

    #磁盘类型
    disk_type = models.CharField(max_length=128,null=True, blank=True)

    #挂载点
    mount  = models.CharField(max_length=128,null=True, blank=True)

    create_time = models.DateTimeField(blank=True, auto_now_add=True)

    update_time = models.DateTimeField(blank=True, auto_now=True)

    tag = models.CharField(max_length=128,blank=True,null=True)

    server = models.ForeignKey('Server',null=True)

    def __unicode__(self):
        return self.name





'''网卡信息'''
class NIC(models.Model):
    name = models.CharField(u'网卡名称', max_length=128,blank=True)
    model = models.CharField(max_length=128,blank=True,null=True)
    ip = models.GenericIPAddressField(max_length=128,blank=True,null=True)
    mac = models.CharField('mac', max_length=64)
    netmask = models.CharField(max_length=64,blank=True,null=True)
    create_time = models.DateTimeField(blank=True, auto_now_add=True)
    update_time = models.DateTimeField(blank=True, auto_now=True)
    tag = models.CharField(max_length=128,blank=True,null=True)

    server = models.ForeignKey('Server')

    def __unicode__(self):
        return self.name






class NetworkDevice(models.Model):
    Assets = models.OneToOneField('Assets')

    name = models.CharField(u'网络设备名称', max_length=128,blank=True)
    #产商
    Firm = models.CharField(max_length=128,null=True, blank=True)
    #型号
    model = models.CharField(max_length=128,blank=True,null=True)
    wan = models.SmallIntegerField(u'WAN口',blank=True, null=True)
    lan = models.SmallIntegerField(u'LAN口',blank=True, null=True)
    manager_ip = models.GenericIPAddressField(blank=True,null=True)
    gateway = models.GenericIPAddressField(blank=True,null=True)
    dram = models.CharField(u'ram', max_length=128,blank=True, null=True)
    flash= models.CharField(u'flash', max_length=128,blank=True, null=True)
    modules = models.SmallIntegerField(u'模块数',blank=True,null=True)

    def __unicode__(self):
        return self.name



class Borrow(models.Model):
    Assets = models.OneToOneField('Assets')
    #用途
    purpose = models.CharField(max_length=128,blank=True, null=True)
    Borrow_time = models.CharField(u'借出时间', max_length=128, null=True)
    Borrow_return_time = models.CharField(u'归还时间', max_length=128, null=True)
    Borrow_user = models.ForeignKey(Employee)

    def __unicode__(self):
        return self.name




