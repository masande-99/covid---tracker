# Generated by Django 3.2.12 on 2022-02-18 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20220218_1623'),
    ]

    operations = [
        migrations.RenameField(
            model_name='results',
            old_name='Any_shortness_breath',
            new_name='Any_shortness_of_breath',
        ),
    ]
