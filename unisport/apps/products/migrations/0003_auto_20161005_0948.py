# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-05 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20161005_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sizes',
            field=models.CharField(max_length=1000),
        ),
    ]
