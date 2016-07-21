# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employeeinfo', '0009_auto_20160601_1131'),
        ('assetsinfo', '0013_mem_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Borrow_time', models.CharField(max_length=128, null=True, verbose_name='\u501f\u51fa\u65f6\u95f4')),
                ('Borrow_return_time', models.CharField(max_length=128, null=True, verbose_name='\u5f52\u8fd8\u65f6\u95f4')),
                ('Assets', models.OneToOneField(to='assetsinfo.Assets')),
                ('Borrow_user', models.ForeignKey(to='employeeinfo.Employee')),
            ],
        ),
        migrations.AlterModelOptions(
            name='cpu',
            options={},
        ),
        migrations.AlterModelOptions(
            name='disk',
            options={},
        ),
        migrations.AlterModelOptions(
            name='kernel_info',
            options={},
        ),
        migrations.AlterModelOptions(
            name='mem',
            options={},
        ),
        migrations.AlterModelOptions(
            name='networkdevice',
            options={},
        ),
        migrations.AlterModelOptions(
            name='nic',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='nic',
            unique_together=set([]),
        ),
    ]
