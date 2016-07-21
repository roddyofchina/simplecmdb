# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assetsinfo', '0014_auto_20160613_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrow',
            name='purpose',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
    ]
