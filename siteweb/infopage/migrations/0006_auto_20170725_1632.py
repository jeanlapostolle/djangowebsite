# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infopage', '0005_auto_20170725_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='slug',
            field=models.CharField(default='1buizW', max_length=6, unique=True),
        ),
    ]
