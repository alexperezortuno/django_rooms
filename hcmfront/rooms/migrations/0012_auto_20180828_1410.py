# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-28 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0011_auto_20180828_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disponibilities',
            name='from_date',
            field=models.TimeField(verbose_name='From'),
        ),
        migrations.AlterField(
            model_name='disponibilities',
            name='to_date',
            field=models.TimeField(verbose_name='To'),
        ),
    ]
