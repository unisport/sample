# -*- coding: utf-8 -*-
# flake8: noqa: E501
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=150)),
                ('price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('price_old', models.DecimalField(max_digits=8, decimal_places=2)),
                ('currency', models.CharField(max_length=3)),
                ('sizes', models.TextField()),
                ('delivery', models.CharField(max_length=8, choices=[('1-2 dage', '1-2 dage')])),
                ('url', models.URLField()),
                ('image', models.URLField()),
                ('img_url', models.URLField()),
                ('is_customizable', models.BooleanField(default=False)),
                ('kids', models.BooleanField(default=False)),
                ('kid_adult', models.BooleanField(default=False)),
                ('women', models.BooleanField(default=True)),
                ('package', models.BooleanField(default=False)),
                ('free_porto', models.BooleanField(default=False)),
                ('online', models.BooleanField(default=False)),
            ],
        ),
    ]
