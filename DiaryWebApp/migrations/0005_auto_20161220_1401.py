# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 14:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DiaryWebApp', '0004_auto_20161220_1346'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='date',
            new_name='dateTime',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='time',
        ),
    ]
