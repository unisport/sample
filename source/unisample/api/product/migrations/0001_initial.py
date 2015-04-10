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
                ('_permanent_id', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('price_old', models.DecimalField(max_digits=8, decimal_places=2)),
                ('kids', models.IntegerField()),
                ('kid_adult', models.IntegerField()),
                ('women', models.IntegerField()),
                ('delivery', models.CharField(max_length=64)),
                ('free_porto', models.BooleanField(default=False)),
                ('package', models.IntegerField()),
                ('sizes', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('img_url', models.URLField()),
            ],
        ),
    ]
