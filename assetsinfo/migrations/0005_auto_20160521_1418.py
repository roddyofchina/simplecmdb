# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assetsinfo', '0004_auto_20160520_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='server',
            name='kernel',
        ),
        migrations.AddField(
            model_name='kernel_info',
            name='server',
            field=models.ForeignKey(to='assetsinfo.Server', null=True),
        ),
    ]
