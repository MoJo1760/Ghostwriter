# Generated by Django 3.2.11 on 2022-02-22 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('user', 'user'), ('manager', 'manager'), ('admin', 'admin'), ('restricted', 'restricted')], default='user', max_length=120),
        ),
    ]
