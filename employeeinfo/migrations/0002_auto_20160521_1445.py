# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employeeinfo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='universit',
            field=models.ForeignKey(to='employeeinfo.universities', null=True),
        ),
        migrations.AlterField(
            model_name='universities',
            name='name',
            field=models.CharField(max_length=128, unique=True, null=True, blank=True),
        ),
    ]
