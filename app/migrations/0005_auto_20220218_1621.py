# Generated by Django 3.2.12 on 2022-02-18 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_incontact_results_in_contact_with_someone_infected'),
    ]

    operations = [
        migrations.RenameField(
            model_name='results',
            old_name='breath',
            new_name='Any_shortness_breath_breath',
        ),
        migrations.RenameField(
            model_name='results',
            old_name='drycough',
            new_name='Do_you_have_a_drycough',
        ),
        migrations.RenameField(
            model_name='results',
            old_name='sorethroat',
            new_name='Do_you_have_a_sorethroat',
        ),
        migrations.RenameField(
            model_name='results',
            old_name='tastesmell',
            new_name='Loss_of_taste_or_smell',
        ),
    ]
