# Generated by Django 3.2.12 on 2022-03-18 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_results_loss_of_taste_or_smell'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='Loss_of_taste_or_smell',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=200, null=True),
        ),
    ]
# Generated by Django 3.2.12 on 2022-03-18 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_results_loss_of_taste_or_smell'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='Loss_of_taste_or_smell',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=200, null=True),
        ),
    ]