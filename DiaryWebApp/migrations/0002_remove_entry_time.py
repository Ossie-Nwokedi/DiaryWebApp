# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-16 17:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DiaryWebApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='time',
        ),
    ]
