# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assetsinfo', '0009_auto_20160525_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idc',
            name='floor',
            field=models.CharField(max_length=20, null=True, verbose_name='\u697c\u5c42'),
        ),
    ]
