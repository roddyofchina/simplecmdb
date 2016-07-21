# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assetsinfo', '0005_auto_20160521_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='description',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='assets',
            name='devicetag',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
