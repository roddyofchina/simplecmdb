# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assetsinfo', '0003_auto_20160520_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networkdevice',
            name='modules',
            field=models.SmallIntegerField(null=True, verbose_name='\u6a21\u5757\u6570', blank=True),
        ),
    ]
