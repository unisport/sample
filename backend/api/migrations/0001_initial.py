# Generated by Django 2.0.1 on 2018-01-16 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('is_customizable', models.BooleanField()),
                ('delivery', models.CharField(max_length=20)),
                ('kids', models.BooleanField()),
                ('name', models.TextField()),
                ('package', models.BooleanField()),
                ('kid_adult', models.BooleanField()),
                ('free_porto', models.BooleanField()),
                ('thumbnail', models.URLField()),
                ('sizes', models.TextField()),
                ('price', models.CharField(max_length=10)),
                ('discount_type', models.CharField(max_length=20)),
                ('online', models.BooleanField()),
                ('price_old', models.CharField(max_length=20)),
                ('currency', models.CharField(max_length=3)),
                ('img_url', models.URLField()),
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
