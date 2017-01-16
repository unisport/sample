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
                ('product_id', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=256)),
                ('kids', models.IntegerField()),
                ('kid_adult', models.IntegerField()),
                ('women', models.IntegerField()),
                ('package', models.IntegerField()),
                ('free_porto', models.BooleanField(default=False)),
                ('price', models.DecimalField(max_digits=12, decimal_places=2)),
                ('price_old', models.DecimalField(max_digits=12, decimal_places=2)),
                ('delivery', models.CharField(max_length=64)),
                ('url', models.CharField(max_length=512)),
                ('img_url', models.CharField(max_length=512, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64, db_index=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.ManyToManyField(to='products.ProductSize'),
            preserve_default=True,
        ),
    ]
