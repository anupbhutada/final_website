# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-06 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extropy', '0005_auto_20171206_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='abstract',
            field=models.TextField(verbose_name='Abstract'),
        ),
    ]