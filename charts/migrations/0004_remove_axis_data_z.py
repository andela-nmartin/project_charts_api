# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-07 12:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0003_axis_data_z'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='axis_data',
            name='z',
        ),
    ]