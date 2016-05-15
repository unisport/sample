# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='kid_adult',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='kids',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='package',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_old',
            field=models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='women',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
    ]
