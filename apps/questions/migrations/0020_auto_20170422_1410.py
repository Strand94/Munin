# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-22 12:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0019_auto_20170406_0225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 22, 14, 10, 7, 887254)),
        ),
        migrations.AlterField(
            model_name='question',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 22, 14, 10, 7, 886253)),
        ),
    ]