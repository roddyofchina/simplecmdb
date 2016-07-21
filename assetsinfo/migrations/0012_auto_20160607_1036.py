# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assetsinfo', '0011_auto_20160602_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='update_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
