# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-07-22 16:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0010_auto_20170722_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='s',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s_grade', to='wechat.student'),
        ),
    ]
