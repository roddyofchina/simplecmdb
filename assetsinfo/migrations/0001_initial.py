# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Assets_name', models.CharField(unique=True, max_length=128, blank=True)),
                ('device_number', models.CharField(unique=True, max_length=128, blank=True)),
                ('Warranty', models.SmallIntegerField(null=True, verbose_name='\u4fdd\u4fee\u671f')),
                ('buy_time', models.DateTimeField(null=True, verbose_name='\u8d2d\u4e70\u65e5\u671f', blank=True)),
                ('buy_type', models.SmallIntegerField(blank=True, null=True, verbose_name='\u8d2d\u4e70\u65b9\u5f0f', choices=[(1, '\u516c\u53f8\u5185\u8d2d'), (2, '\u5458\u5de5\u81ea\u8d2d')])),
                ('price', models.IntegerField(null=True, verbose_name='\u8d2d\u4e70\u4ef7\u683c', blank=True)),
                ('suse_time', models.DateTimeField(null=True, verbose_name='\u5f00\u59cb\u4f7f\u7528\u65f6\u95f4')),
                ('euse_time', models.DateTimeField(null=True, verbose_name='\u622a\u81f3\u4f7f\u7528\u65f6\u95f4')),
                ('status', models.SmallIntegerField(blank=True, null=True, verbose_name='\u72b6\u6001', choices=[(1, '\u6b63\u5728\u4f7f\u7528'), (2, '\u672a\u4f7f\u7528'), (3, '\u8bbe\u5907\u6545\u969c'), (4, '\u5e93\u5b58\u5907\u7528')])),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u8d44\u4ea7\u521b\u5efa\u65f6\u95f4', null=True)),
                ('devicetag', models.CharField(max_length=255, unique=True, null=True, blank=True)),
                ('description', models.CharField(max_length=255, unique=True, null=True, blank=True)),
            ],
            options={
                'permissions': (('cmdb_assets_add', '\u6dfb\u52a0\u8d44\u4ea7'), ('cmdb_assets_view', '\u67e5\u770b\u8d44\u4ea7'), ('cmdb_assets_change', '\u4fee\u6539\u8d44\u4ea7'), ('cmdb_assets_delete', '\u5220\u9664\u8d44\u4ea7')),
            },
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128, blank=True)),
            ],
            options={
                'permissions': (('cmdb_devicetype_add', '\u6dfb\u52a0\u4e1a\u52a1'), ('cmdb_devicetype_view', '\u67e5\u770b\u4e1a\u52a1'), ('cmdb_devicetype_change', '\u4fee\u6539\u4e1a\u52a1'), ('cmdb_devicetype_delete', '\u5220\u9664\u4e1a\u52a1')),
            },
        ),
        migrations.CreateModel(
            name='Cpu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Architecture', models.CharField(max_length=128, null=True, blank=True)),
                ('Vendor_id', models.CharField(max_length=128, null=True, blank=True)),
                ('model', models.CharField(max_length=128, null=True, blank=True)),
                ('cpus', models.SmallIntegerField(null=True)),
                ('cpu_mhz', models.CharField(max_length=128, null=True, blank=True)),
                ('L1cache', models.CharField(max_length=128, null=True, blank=True)),
                ('L2cache', models.CharField(max_length=128, null=True, blank=True)),
                ('L3cache', models.CharField(max_length=128, null=True, blank=True)),
                ('Thread', models.SmallIntegerField(null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('tag', models.CharField(max_length=128, null=True, blank=True)),
            ],
            options={
                'permissions': (('cmdb_cpu_add', '\u6dfb\u52a0CPU'), ('cmdb_cpu_view', '\u67e5\u770bCPU'), ('cmdb_cpu_change', '\u4fee\u6539CPU'), ('cmdb_cpu_delete', '\u5220\u9664CPU')),
            },
        ),
        migrations.CreateModel(
            name='DeviceType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, blank=True)),
            ],
            options={
                'permissions': (('cmdb_devicetype_add', '\u6dfb\u52a0\u8bbe\u5907\u7c7b\u578b'), ('cmdb_devicetype_view', '\u67e5\u770b\u8bbe\u5907\u7c7b\u578b'), ('cmdb_devicetype_change', '\u4fee\u6539\u8bbe\u5907\u7c7b\u578b'), ('cmdb_devicetype_delete', '\u5220\u9664\u8bbe\u5907\u7c7b\u578b')),
            },
        ),
        migrations.CreateModel(
            name='Disk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, blank=True)),
                ('sn', models.CharField(max_length=128, blank=True)),
                ('Firm', models.CharField(max_length=128, null=True, blank=True)),
                ('capacity', models.CharField(max_length=128, null=True, blank=True)),
                ('disk_type', models.CharField(max_length=128, null=True, blank=True)),
                ('mount', models.CharField(max_length=128, null=True, blank=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('tag', models.CharField(max_length=128, null=True, blank=True)),
            ],
            options={
                'permissions': (('cmdb_disk_add', '\u6dfb\u52a0\u786c\u76d8'), ('cmdb_disk_view', '\u67e5\u770b\u786c\u76d8'), ('cmdb_disk_change', '\u4fee\u6539\u786c\u76d8'), ('cmdb_disk_delete', '\u5220\u9664\u786c\u76d8')),
            },
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idc_name', models.CharField(unique=True, max_length=128, blank=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('contacts', models.CharField(max_length=128, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('floor', models.SmallIntegerField(null=True, verbose_name='\u697c\u5c42')),
            ],
            options={
                'permissions': (('cmdb_idc_add', '\u6dfb\u52a0IDC'), ('cmdb_idc_view', '\u67e5\u770bIDC'), ('cmdb_idc_change', '\u4fee\u6539IDC'), ('cmdb_idc_delete', '\u5220\u9664IDC')),
            },
        ),
        migrations.CreateModel(
            name='kernel_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('platform', models.CharField(max_length=128, null=True, blank=True)),
                ('system', models.CharField(max_length=128, null=True, blank=True)),
                ('version', models.CharField(max_length=128, null=True, blank=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'permissions': (('cmdb_kernel_add', '\u6dfb\u52a0\u7cfb\u7edf\u4fe1\u606f'), ('cmdb_kernel_view', '\u67e5\u770b\u7cfb\u7edf\u4fe1\u606f'), ('cmdb_kernel_change', '\u4fee\u6539\u7cfb\u7edf\u4fe1\u606f'), ('cmdb_kernel_delete', '\u5220\u9664\u7cfb\u7edf\u4fe1\u606f')),
            },
        ),
        migrations.CreateModel(
            name='Mem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('capacity', models.CharField(max_length=128, null=True, blank=True)),
                ('swap', models.CharField(max_length=128, null=True, blank=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('tag', models.CharField(max_length=128, null=True, blank=True)),
            ],
            options={
                'permissions': (('cmdb_mem_add', '\u6dfb\u52a0\u5185\u5b58'), ('cmdb_mem_view', '\u67e5\u770b\u5185\u5b58'), ('cmdb_mem_change', '\u4fee\u6539\u5185\u5b58'), ('cmdb_mem_delete', '\u5220\u9664\u5185\u5b58')),
            },
        ),
        migrations.CreateModel(
            name='NetworkDevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='\u7f51\u5361\u540d\u79f0', blank=True)),
                ('Firm', models.CharField(max_length=128, null=True, blank=True)),
                ('model', models.CharField(max_length=128, null=True, blank=True)),
                ('wan', models.SmallIntegerField(null=True, verbose_name='WAN\u53e3', blank=True)),
                ('lan', models.SmallIntegerField(null=True, verbose_name='LAN\u53e3', blank=True)),
                ('manager_ip', models.GenericIPAddressField(null=True, blank=True)),
                ('gateway', models.GenericIPAddressField(null=True, blank=True)),
                ('dram', models.CharField(max_length=128, null=True, verbose_name='ram', blank=True)),
                ('flash', models.CharField(max_length=128, null=True, verbose_name='flash', blank=True)),
                ('modules', models.SmallIntegerField(verbose_name='LAN\u53e3', blank=True)),
                ('Assets', models.OneToOneField(to='assetsinfo.Assets')),
            ],
            options={
                'permissions': (('cmdb_network_add', '\u6dfb\u52a0\u7f51\u7edc\u8bbe\u5907\u4fe1\u606f'), ('cmdb_network_view', '\u67e5\u770b\u7f51\u7edc\u8bbe\u5907\u4fe1\u606f'), ('cmdb_network_change', '\u4fee\u6539\u7f51\u7edc\u8bbe\u5907\u4fe1\u606f'), ('cmdb_network_delete', '\u5220\u9664\u7f51\u7edc\u8bbe\u5907\u4fe1\u606f')),
            },
        ),
        migrations.CreateModel(
            name='NIC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='\u7f51\u5361\u540d\u79f0', blank=True)),
                ('model', models.CharField(max_length=128, null=True, blank=True)),
                ('ip', models.GenericIPAddressField(null=True, blank=True)),
                ('mac', models.CharField(max_length=64, verbose_name=b'mac')),
                ('netmask', models.CharField(max_length=64, null=True, blank=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('tag', models.CharField(max_length=128, null=True, blank=True)),
            ],
            options={
                'permissions': (('cmdb_nic_add', '\u6dfb\u52a0\u7f51\u5361'), ('cmdb_nic_view', '\u67e5\u770b\u7f51\u5361'), ('cmdb_nic_change', '\u4fee\u6539\u7f51\u5361'), ('cmdb_nic_delete', '\u5220\u9664\u7f51\u5361')),
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('provider_name', models.CharField(unique=True, max_length=128, blank=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('contacts', models.CharField(max_length=128, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('Fax', models.CharField(max_length=20, null=True)),
            ],
            options={
                'permissions': (('cmdb_provider_add', '\u6dfb\u52a0\u63d0\u4f9b\u5546'), ('cmdb_provider_view', '\u67e5\u770b\u63d0\u4f9b\u5546'), ('cmdb_provider_change', '\u4fee\u6539\u63d0\u4f9b\u5546'), ('cmdb_provider_delete', '\u5220\u9664\u63d0\u4f9b\u5546')),
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sninfo', models.CharField(max_length=128)),
                ('Firm', models.CharField(max_length=128, null=True, blank=True)),
                ('model', models.CharField(max_length=128, null=True, blank=True)),
                ('raid', models.CharField(max_length=128, null=True, blank=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('Assets', models.OneToOneField(to='assetsinfo.Assets')),
                ('kernel', models.ForeignKey(to='assetsinfo.kernel_info', null=True)),
            ],
            options={
                'permissions': (('cmdb_server_add', '\u6dfb\u52a0\u670d\u52a1\u5668'), ('cmdb_server_view', '\u67e5\u770b\u670d\u52a1\u5668'), ('cmdb_server_change', '\u4fee\u6539\u670d\u52a1\u5668'), ('cmdb_server_delete', '\u5220\u9664\u670d\u52a1\u5668')),
            },
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, blank=True)),
                ('version', models.CharField(max_length=128, null=True, blank=True)),
                ('license', models.CharField(max_length=128, null=True, blank=True)),
            ],
            options={
                'permissions': (('cmdb_software_add', '\u6dfb\u52a0\u8f6f\u4ef6'), ('cmdb_software_view', '\u67e5\u770b\u8f6f\u4ef6'), ('cmdb_software_change', '\u4fee\u6539\u8f6f\u4ef6'), ('cmdb_software_delete', '\u5220\u9664\u8f6f\u4ef6')),
            },
        ),
        migrations.AddField(
            model_name='server',
            name='software',
            field=models.ManyToManyField(to='assetsinfo.Software', blank=True),
        ),
        migrations.AddField(
            model_name='nic',
            name='server',
            field=models.ForeignKey(to='assetsinfo.Server'),
        ),
        migrations.AddField(
            model_name='mem',
            name='server',
            field=models.ForeignKey(to='assetsinfo.Server', null=True),
        ),
        migrations.AddField(
            model_name='disk',
            name='server',
            field=models.ForeignKey(to='assetsinfo.Server', null=True),
        ),
        migrations.AddField(
            model_name='cpu',
            name='server',
            field=models.ForeignKey(to='assetsinfo.Server', null=True),
        ),
    ]
