# Generated by Django 3.2.11 on 2022-07-06 17:04

# Django Imports
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rolodex', '0030_auto_20220526_1737'),
    ]

    operations = [
        migrations.RunSQL(
            'ALTER TABLE rolodex_projectobjective ALTER COLUMN position SET DEFAULT 1;'
        ),
        migrations.RunSQL(
            'ALTER TABLE rolodex_projectobjective ALTER COLUMN priority_id SET DEFAULT 1;'
        ),
    ]
