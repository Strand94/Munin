# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 11:18
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20170216_2135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('course_id', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('year', models.DateTimeField(default=datetime.datetime)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='staticpages.School'),
        ),
        migrations.AddField(
            model_name='course',
            name='lecturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
