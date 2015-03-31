# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=512)),
                ('kids', models.CharField(default='0', max_length=1, choices=[('0', 'No'), ('1', 'Yes')])),
                ('women', models.CharField(default='0', max_length=1, choices=[('0', 'No'), ('1', 'Yes')])),
                ('kid_adult', models.CharField(default='0', max_length=1, choices=[('0', 'No'), ('1', 'Yes')])),
                ('package', models.CharField(default='0', max_length=1, choices=[('0', 'No'), ('1', 'Yes')])),
                ('free_porto', models.BooleanField(default=False)),
                ('delivery', models.CharField(max_length=64)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('price_old', models.DecimalField(max_digits=10, decimal_places=2)),
                ('url', models.CharField(max_length=512, validators=[django.core.validators.URLValidator])),
                ('img_url', models.CharField(max_length=512, validators=[django.core.validators.URLValidator])),
            ],
            options={
                'ordering': ('-price',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('size', models.CharField(unique=True, max_length=16)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.ManyToManyField(to='products.Size'),
            preserve_default=True,
        ),
    ]
