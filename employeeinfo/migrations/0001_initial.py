# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0002_auto_20160519_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128, blank=True)),
                ('number', models.IntegerField(null=True, verbose_name='\u5458\u5de5\u7f16\u53f7', blank=True)),
                ('sex', models.SmallIntegerField(null=True, verbose_name='\u59d3\u522b')),
                ('contact', models.CharField(max_length=128, null=True)),
                ('email', models.CharField(max_length=128, unique=True, null=True, blank=True)),
                ('age', models.SmallIntegerField(null=True, verbose_name='\u5e74\u9f84')),
                ('status', models.SmallIntegerField(blank=True, null=True, verbose_name='\u72b6\u6001', choices=[(1, b'\xe5\x9c\xa8\xe8\x81\x8c'), (2, b'\xe7\xa6\xbb\xe8\x81\x8c')])),
                ('birthday', models.DateTimeField(null=True, verbose_name='\u51fa\u751f\u65e5\u671f', blank=True)),
                ('EntryTime', models.DateTimeField(null=True, verbose_name='\u5165\u804c\u65e5\u671f', blank=True)),
                ('exitTime', models.DateTimeField(null=True, verbose_name='\u79bb\u804c\u65e5\u671f', blank=True)),
                ('family_address', models.CharField(max_length=255, unique=True, null=True, blank=True)),
                ('description', models.CharField(max_length=255, unique=True, null=True, blank=True)),
                ('photo', models.ImageField(null=True, upload_to=b'photos/', blank=True)),
                ('dept', models.ForeignKey(to='useraccount.Department', null=True)),
            ],
            options={
                'db_table': 'employee',
                'permissions': (('cmdb_employee_add', '\u6dfb\u52a0\u5458\u5de5\u4fe1\u606f'), ('cmdb_employee_view', '\u67e5\u770b\u5458\u5de5\u4fe1\u606f'), ('cmdb_employee_change', '\u4fee\u6539\u5458\u5de5\u4fe1\u606f'), ('cmdb_employee_delete', '\u5220\u9664\u5458\u5de5\u4fe1\u606f')),
            },
        ),
        migrations.CreateModel(
            name='jobtitle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128, blank=True)),
            ],
            options={
                'permissions': (('cmdb_jobtitle_add', '\u6dfb\u52a0\u804c\u4f4d'), ('cmdb_jobtitle_view', '\u67e5\u770b\u804c\u4f4d'), ('cmdb_jobtitle_change', '\u4fee\u6539\u804c\u4f4d'), ('cmdb_jobtitle_delete', '\u5220\u9664\u804c\u4f4d')),
            },
        ),
        migrations.CreateModel(
            name='universities',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128, blank=True)),
            ],
            options={
                'permissions': (('cmdb_universities_add', '\u6dfb\u52a0\u6bd5\u4e1a\u9662\u6821'), ('cmdb_universities_view', '\u67e5\u770b\u6bd5\u4e1a\u9662\u6821'), ('cmdb_universities_change', '\u4fee\u6539\u6bd5\u4e1a\u9662\u6821'), ('cmdb_universities_delete', '\u5220\u9664\u6bd5\u4e1a\u9662\u6821')),
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='jobtitle',
            field=models.ForeignKey(to='employeeinfo.jobtitle'),
        ),
    ]
