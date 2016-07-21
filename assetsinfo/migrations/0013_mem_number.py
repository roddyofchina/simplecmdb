# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assetsinfo', '0012_auto_20160607_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='mem',
            name='number',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
    ]
