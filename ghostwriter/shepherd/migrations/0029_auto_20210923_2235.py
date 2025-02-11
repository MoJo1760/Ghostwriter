# Generated by Django 3.1.13 on 2021-09-23 22:35

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shepherd', '0028_auto_20210923_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transientserver',
            name='aux_address',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.GenericIPAddressField(blank=True, help_text='Enter additional IP addresses', null=True, verbose_name='Auxiliary IP Address'), blank=True, default=list, help_text='Enter a comma-separated list of IP addresses', size=5),
        ),
    ]
