# Generated by Django 2.1.7 on 2019-03-30 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0006_auto_20190330_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='kid_adult',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='kids',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
