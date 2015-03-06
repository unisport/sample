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
                ('fake_id', models.PositiveIntegerField(unique=True)),
                ('name', models.CharField(max_length=255)),
                ('sizes', models.CharField(max_length=255)),
                ('price', models.DecimalField(max_digits=16, decimal_places=2)),
                ('price_old', models.DecimalField(max_digits=16, decimal_places=2)),
                ('delivery', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('img_url', models.CharField(max_length=255)),
                ('kids', models.BooleanField()),
                ('kid_adult', models.BooleanField()),
                ('women', models.BooleanField()),
                ('package', models.BooleanField()),
                ('free_porto', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
