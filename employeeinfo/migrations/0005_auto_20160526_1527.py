# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employeeinfo', '0004_auto_20160524_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='sex',
            field=models.SmallIntegerField(blank=True, null=True, verbose_name='\u59d3\u522b', choices=[(1, b'\xe7\x94\xb7'), (2, b'\xe5\xa5\xb3')]),
        ),
    ]
