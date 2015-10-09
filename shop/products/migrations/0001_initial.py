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
                ('id_ext', models.TextField()),
                ('kids', models.IntegerField()),
                ('name', models.TextField()),
                ('sizes', models.TextField()),
                ('kid_adult', models.TextField()),
                ('free_porto', models.TextField()),
                ('price', models.TextField()),
                ('package', models.TextField()),
                ('delivery', models.TextField()),
                ('url', models.TextField()),
                ('price_old', models.TextField()),
                ('img_url', models.TextField()),
                ('women', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
