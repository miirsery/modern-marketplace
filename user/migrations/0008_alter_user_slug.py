# Generated by Django 3.2 on 2022-06-30 16:56

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_user_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='username'),
        ),
    ]
