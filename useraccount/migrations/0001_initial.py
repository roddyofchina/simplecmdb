# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('realname', models.CharField(default=b'admin', max_length=20, null=True)),
                ('phone', models.CharField(max_length=12, null=True)),
                ('photo', models.ImageField(null=True, upload_to=b'photos/', blank=True)),
                ('QQ', models.CharField(default=b'/photos/userphoto.jpg', max_length=50, null=True)),
            ],
            options={
                'permissions': (('cmdb_users_add', '\u6dfb\u52a0\u7528\u6237'), ('cmdb_users_view', '\u67e5\u770b\u7528\u6237'), ('cmdb_users_view_info', '\u67e5\u770b\u7528\u6237\u8be6\u7ec6'), ('cmdb_users_change', '\u4fee\u6539\u7528\u6237'), ('cmdb_users_delete', '\u5220\u9664\u7528\u6237'), ('cmdb_users_restpass', '\u4fee\u6539\u7528\u6237\u5bc6\u7801')),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64)),
            ],
            options={
                'permissions': (('cmdb_dept_add', '\u6dfb\u52a0\u90e8\u95e8\u4fe1\u606f'), ('cmdb_dept_view', '\u67e5\u770b\u90e8\u95e8\u4fe1\u606f'), ('cmdb_dept_change', '\u4fee\u6539\u90e8\u95e8\u4fe1\u606f'), ('cmdb_dept_delete', '\u5220\u9664\u90e8\u95e8\u4fe1\u606f')),
            },
        ),
        migrations.CreateModel(
            name='History_Login',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('login_time', models.DateTimeField(auto_now_add=True)),
                ('logout_time', models.DateTimeField(auto_now=True)),
                ('user_ip', models.GenericIPAddressField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('cmdb_history_view', '\u67e5\u770b\u767b\u5f55\u5386\u53f2'), ('cmdb_history_delete', '\u5220\u9664\u767b\u5f55\u5386\u53f2')),
            },
        ),
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.ForeignKey(to='useraccount.Department', null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions'),
        ),
    ]
