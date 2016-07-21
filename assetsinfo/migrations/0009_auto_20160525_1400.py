# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assetsinfo', '0008_auto_20160524_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='principal',
            field=models.ForeignKey(related_name='principal_s', default=None, to='employeeinfo.Employee', null=True),
        ),
    ]
