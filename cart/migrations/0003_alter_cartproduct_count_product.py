# Generated by Django 3.2 on 2022-05-27 15:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cart_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartproduct',
            name='count_product',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(2147483647)], verbose_name='Количество'),
        ),
    ]
