# Generated by Django 2.1.7 on 2019-04-10 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0016_auto_20190403_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img_url',
            field=models.CharField(default='URL', max_length=255),
        ),
    ]
