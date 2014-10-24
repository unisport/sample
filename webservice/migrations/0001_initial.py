# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('kids', models.BooleanField(default=None)),
                ('name', models.CharField(max_length=256)),
                ('sizes', models.CharField(max_length=256)),
                ('kid_adult', models.BooleanField(default=None)),
                ('free_porto', models.BooleanField(default=None)),
                ('price', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('price_old', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('package', models.BooleanField(default=None)),
                ('delivery', models.CharField(default=0, max_length=20)),
                ('url', models.URLField(blank=True, null=True, validators=[django.core.validators.URLValidator()])),
                ('img_url', models.URLField(blank=True, null=True, validators=[django.core.validators.URLValidator()])),
                ('women', models.BooleanField(default=None)),
                ('id', models.CharField(max_length=8, serialize=False, primary_key=True)),
            ],
            options={
                'ordering': ['price'],
            },
            bases=(models.Model,),
        ),
    ]
