# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employeeinfo', '0008_auto_20160601_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='description',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='family_address',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='number',
            field=models.IntegerField(unique=True, null=True, verbose_name='\u5458\u5de5\u7f16\u53f7', blank=True),
        ),
    ]
