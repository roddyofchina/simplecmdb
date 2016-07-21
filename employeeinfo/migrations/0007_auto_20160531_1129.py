# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employeeinfo', '0006_auto_20160526_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='EntryTime',
            field=models.CharField(max_length=128, null=True, verbose_name='\u5165\u804c\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='ExitTime',
            field=models.CharField(max_length=128, null=True, verbose_name='\u79bb\u804c\u65f6\u95f4'),
        ),
    ]
