# Generated by Django 3.2.12 on 2022-03-18 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20220318_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='temperature',
            field=models.FloatField(null=True),
        ),
    ]
