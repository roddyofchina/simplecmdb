# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employeeinfo', '0001_initial'),
        ('assetsinfo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assets',
            name='Employee',
            field=models.ForeignKey(related_name='Employee_set', to='employeeinfo.Employee'),
        ),
        migrations.AddField(
            model_name='assets',
            name='IDC',
            field=models.ForeignKey(blank=True, to='assetsinfo.IDC', null=True),
        ),
        migrations.AddField(
            model_name='assets',
            name='admin',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='assets',
            name='business',
            field=models.ForeignKey(to='assetsinfo.Business'),
        ),
        migrations.AddField(
            model_name='assets',
            name='device_type',
            field=models.ForeignKey(to='assetsinfo.DeviceType'),
        ),
        migrations.AddField(
            model_name='assets',
            name='principal',
            field=models.ManyToManyField(related_name='principal_set', to='employeeinfo.Employee'),
        ),
        migrations.AddField(
            model_name='assets',
            name='provider',
            field=models.ForeignKey(to='assetsinfo.Provider'),
        ),
        migrations.AlterUniqueTogether(
            name='nic',
            unique_together=set([('name', 'mac')]),
        ),
    ]
