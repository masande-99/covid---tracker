# Generated by Django 3.2.12 on 2022-02-11 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_results_temperature'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
# Generated by Django 3.2.12 on 2022-02-11 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_results_temperature'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='date',
            field=models.DateField(null=True),
        ),
    ]