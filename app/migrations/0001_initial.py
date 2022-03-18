# Generated by Django 3.2.12 on 2022-02-11 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('lastname', models.CharField(max_length=200, null=True)),
                ('department', models.CharField(max_length=200, null=True)),
                ('incontact', models.CharField(max_length=200, null=True)),
                ('drycough', models.CharField(max_length=200, null=True)),
                ('sorethroat', models.CharField(max_length=200, null=True)),
                ('temperature', models.CharField(max_length=200, null=True)),
                ('breath', models.CharField(max_length=200, null=True)),
                ('tastesmell', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]