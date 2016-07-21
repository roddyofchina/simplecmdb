# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employeeinfo', '0007_auto_20160531_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='birthday',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
    ]
