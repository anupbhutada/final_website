# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-06 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extropy', '0003_auto_20171129_0421'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='abstract',
            field=models.CharField(default='blank', max_length=10000, verbose_name='Abstract'),
            preserve_default=False,
        ),
    ]
