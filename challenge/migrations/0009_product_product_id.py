# Generated by Django 2.1.7 on 2019-03-30 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0008_remove_product_discount_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_id',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
