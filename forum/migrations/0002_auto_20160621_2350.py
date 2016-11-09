# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 18:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ans', models.CharField(max_length=10000)),
                ('ans_author', models.CharField(max_length=30)),
                ('ans_date', models.DateTimeField(blank=True, default=datetime.datetime(2016, 6, 21, 23, 50, 29, 370387))),
            ],
        ),
        migrations.RemoveField(
            model_name='answere',
            name='question',
        ),
        migrations.AlterField(
            model_name='question',
            name='ques_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 6, 21, 23, 50, 29, 363035)),
        ),
        migrations.DeleteModel(
            name='Answere',
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Question'),
        ),
    ]