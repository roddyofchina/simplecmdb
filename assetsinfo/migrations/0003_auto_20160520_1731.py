# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assetsinfo', '0002_auto_20160520_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networkdevice',
            name='name',
            field=models.CharField(max_length=128, verbose_name='\u7f51\u7edc\u8bbe\u5907\u540d\u79f0', blank=True),
        ),
    ]
