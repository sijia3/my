# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-07-28 09:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0012_auto_20170723_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s_grade', to='wechat.student', verbose_name='\u5b66\u751f'),
        ),
    ]