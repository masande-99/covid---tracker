from django.db import models

# Create your models here.

class Results(models.Model):
    DEPARTMENT = (
        ('Development', 'Development'),
        ('Data Team', 'Data Team'),
        ('Quality Assurance', 'Quality Assurance')
    )

    YN = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )

    YesNo = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )

    name = models.CharField(max_length=200, null=True)
    lastname = models.CharField(max_length=200, null=True)
    department = models.CharField(max_length=200, null=True, choices=DEPARTMENT)
    In_contact_with_someone_infected = models.CharField(max_length=200, null=True, choices=YN)
    Do_you_have_a_dry_cough = models.CharField(max_length=200, null=True, choices=YesNo)
    Do_you_have_a_sore_throat = models.CharField(max_length=200, null=True, choices=YN)
    Your_temperature = models.FloatField(null=True)
    Any_shortness_of_breath = models.CharField(max_length=200, null=True, choices=YesNo)
    Loss_of_taste_or_smell = models.CharField(max_length=200, null=True, choices=YN)
    The_date_today = models.DateField(null=True)

    def __str__(self):
        return self.name