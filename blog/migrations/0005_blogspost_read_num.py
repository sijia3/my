# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-08-01 05:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170731_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogspost',
            name='read_num',
            field=models.IntegerField(default=0, verbose_name=b'\xe9\x98\x85\xe8\xaf\xbb\xe6\xac\xa1\xe6\x95\xb0'),
        ),
    ]
