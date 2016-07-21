# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assetsinfo', '0010_auto_20160602_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idc',
            name='address',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='idc',
            name='contacts',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='idc',
            name='floor',
            field=models.CharField(max_length=20, null=True, verbose_name='\u697c\u5c42', blank=True),
        ),
        migrations.AlterField(
            model_name='idc',
            name='phone',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
