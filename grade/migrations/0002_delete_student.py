# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-07-15 14:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grade', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='student',
        ),
    ]