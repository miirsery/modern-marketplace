# Generated by Django 3.2 on 2022-06-13 12:07

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='username', verbose_name='URL'),
        ),
    ]
