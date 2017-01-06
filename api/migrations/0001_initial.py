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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=256)),
                ('sizes', models.CharField(max_length=256)),
                ('delivery', models.CharField(max_length=128)),
                ('kids', models.BooleanField(default=False)),
                ('kid_adult', models.BooleanField(default=False)),
                ('free_porto', models.BooleanField(default=False)),
                ('package', models.BooleanField(default=False)),
                ('women', models.BooleanField(default=False)),
                ('price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('price_old', models.DecimalField(max_digits=8, decimal_places=2)),
                ('url', models.URLField()),
                ('img_url', models.URLField()),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
