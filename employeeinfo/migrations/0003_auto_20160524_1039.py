# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employeeinfo', '0002_auto_20160521_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='universit',
            field=models.CharField(unique=True, max_length=128, blank=True),
        ),
        migrations.DeleteModel(
            name='universities',
        ),
    ]
