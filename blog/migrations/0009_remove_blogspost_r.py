# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-08-09 08:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_blogspost_r'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogspost',
            name='r',
        ),
    ]
