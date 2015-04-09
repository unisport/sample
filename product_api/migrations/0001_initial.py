# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('price_old', models.DecimalField(max_digits=8, decimal_places=2)),
                ('delivery', models.CharField(max_length=16)),
                ('free_porto', models.CharField(max_length=5)),
                ('package', models.CharField(max_length=1)),
                ('kids', models.CharField(max_length=1)),
                ('kid_adult', models.CharField(max_length=1)),
                ('women', models.CharField(max_length=1)),
                ('sizes', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('img_url', models.URLField()),
            ],
        ),
    ]
