# Generated by Django 3.2.12 on 2022-03-18 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_rename_temperature_results_your_temperature'),
    ]

    operations = [
        migrations.RenameField(
            model_name='results',
            old_name='date',
            new_name='Todays_date',
        ),
    ]
