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
                ('name', models.CharField(max_length=360)),
                ('image', models.ImageField(null=True, upload_to=b'products/', blank=True)),
                ('currency', models.CharField(max_length=50)),
                ('delivery', models.CharField(max_length=200)),
                ('kids', models.IntegerField()),
                ('package', models.IntegerField()),
                ('kid_adult', models.IntegerField()),
                ('price', models.DecimalField(max_digits=12, decimal_places=2)),
                ('price_old', models.DecimalField(max_digits=12, decimal_places=2)),
                ('women', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('size', models.CharField(default=b'One Size', max_length=720)),
                ('product_size', models.ForeignKey(to='products.Product')),
            ],
        ),
    ]
