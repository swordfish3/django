# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-07 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170507_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='barcode',
            field=models.BigIntegerField(max_length=100),
        ),
    ]
