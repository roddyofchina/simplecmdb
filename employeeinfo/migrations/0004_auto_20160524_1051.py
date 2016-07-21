# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employeeinfo', '0003_auto_20160524_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='universit',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
    ]
