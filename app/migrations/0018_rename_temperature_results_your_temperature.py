# Generated by Django 3.2.12 on 2022-03-18 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20220318_0920'),
    ]

    operations = [
        migrations.RenameField(
            model_name='results',
            old_name='temperature',
            new_name='Your_temperature',
        ),
    ]