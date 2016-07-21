# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assetsinfo', '0006_auto_20160523_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='buy_time',
            field=models.CharField(max_length=128, null=True, verbose_name='\u8d2d\u4e70\u65e5\u671f', blank=True),
        ),
        migrations.AlterField(
            model_name='assets',
            name='euse_time',
            field=models.CharField(max_length=128, null=True, verbose_name='\u622a\u81f3\u4f7f\u7528\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='assets',
            name='suse_time',
            field=models.CharField(max_length=128, null=True, verbose_name='\u5f00\u59cb\u4f7f\u7528\u65f6\u95f4'),
        ),
    ]
