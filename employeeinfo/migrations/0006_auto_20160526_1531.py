# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employeeinfo', '0005_auto_20160526_1527'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='exitTime',
            new_name='ExitTime',
        ),
    ]
