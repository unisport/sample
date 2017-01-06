# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(default=0, max_length=60)),
                ('price', models.DecimalField(default=0.0, max_digits=6, decimal_places=2)),
                ('price_old', models.DecimalField(default=0.0, max_digits=6, decimal_places=2)),
                ('sizes', models.TextField(default=b'', max_length=350)),
                ('kid_adult', models.CharField(default=b'0', max_length=1, choices=[(b'0', False), (b'1', True)])),
                ('kids', models.CharField(default=b'0', max_length=1, choices=[(b'0', False), (b'1', True)])),
                ('free_porto', models.CharField(default=b'0', max_length=1, choices=[(b'0', False), (b'1', True)])),
                ('women', models.CharField(default=b'0', max_length=1, choices=[(b'0', False), (b'1', True)])),
                ('package', models.CharField(default=b'0', max_length=1, choices=[(b'0', False), (b'1', True)])),
                ('delivery', models.CharField(default=b'1-2 dage', max_length=12)),
                ('img_url', models.URLField(default=b'', max_length=100)),
                ('url', models.URLField(default=b'', max_length=100)),
            ],
        ),
    ]
