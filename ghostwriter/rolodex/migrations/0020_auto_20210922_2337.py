# Generated by Django 3.1.13 on 2021-09-22 23:37

from django.db import migrations, models
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rolodex', '0019_auto_20210303_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='address',
            field=models.TextField(blank=True, help_text='An address to be used for reports or shipping', null=True, verbose_name='Client Business Address'),
        ),
        migrations.AddField(
            model_name='client',
            name='timezone',
            field=timezone_field.fields.TimeZoneField(default='America/Los_Angeles', help_text='Primary timezone of the client', verbose_name='Client Timezone'),
        ),
    ]
