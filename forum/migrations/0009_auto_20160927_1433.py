# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-27 09:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_auto_20160710_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='ans_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 9, 27, 14, 33, 19, 248564)),
        ),
        migrations.AlterField(
            model_name='question',
            name='ques_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 9, 27, 14, 33, 19, 248071)),
        ),
    ]
