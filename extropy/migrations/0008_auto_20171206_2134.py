# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-06 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extropy', '0007_auto_20171206_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='abstract',
            field=models.TextField(max_length=10000, verbose_name='Abstract'),
        ),
    ]
