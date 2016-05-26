# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django.contrib.auth.models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status', default=False)),
                ('username', models.CharField(validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-_]+$', 32), 'O nome de usuário só pode conter letras ou dígitos ou os seguintes caracteres: @/./+/-/_', 'invalid')], verbose_name='Nome do Usuário', unique=True, max_length=30)),
                ('email', models.EmailField(verbose_name='E-mail', unique=True, max_length=254)),
                ('name', models.CharField(verbose_name='Nome', blank=True, max_length=100)),
                ('is_active', models.BooleanField(verbose_name='Está ativo?', default=True)),
                ('is_staff', models.BooleanField(verbose_name='Equipe Administrativa?', default=False)),
                ('date_joined', models.DateTimeField(verbose_name='Data de Entrada', auto_now_add=True)),
                ('groups', models.ManyToManyField(verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', blank=True, related_name='user_set', related_query_name='user', to='auth.Group')),
                ('user_permissions', models.ManyToManyField(verbose_name='user permissions', help_text='Specific permissions for this user.', blank=True, related_name='user_set', related_query_name='user', to='auth.Permission')),
            ],
            options={
                'verbose_name_plural': 'Usuários',
                'verbose_name': 'Usuário',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
