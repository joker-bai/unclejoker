# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-07 08:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_user_pwd'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='mobile',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='pwd',
            field=models.CharField(default='123456', max_length=32),
        ),
    ]
