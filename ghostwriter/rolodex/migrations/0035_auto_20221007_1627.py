# Generated by Django 3.2.11 on 2022-10-07 16:27

# Django Imports
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rolodex', '0034_alter_deconfliction_options'),
    ]

    operations = [
        migrations.RunSQL(
            'ALTER TABLE rolodex_deconfliction ALTER COLUMN created_at SET DEFAULT CURRENT_TIMESTAMP;'
        ),
    ]
