# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employeeinfo', '0002_auto_20160521_1445'),
        ('assetsinfo', '0007_auto_20160523_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='Employee',
            field=models.ForeignKey(related_name='Employee_set', to='employeeinfo.Employee', null=True),
        ),
        migrations.RemoveField(
            model_name='assets',
            name='principal',
        ),
        migrations.AddField(
            model_name='assets',
            name='principal',
            field=models.ForeignKey(related_name='principal_s', to='employeeinfo.Employee', null=True),
        ),
    ]
