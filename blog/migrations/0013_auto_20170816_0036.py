# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-08-15 16:36
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20170813_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogspost',
            name='content',
            field=DjangoUeditor.models.UEditorField(verbose_name=b'\xe5\x86\x85\xe5\xae\xb9'),
        ),
    ]