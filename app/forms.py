from django.forms import ModelForm
from django import forms
from .models import *


class ResultsForm(ModelForm):
    class Meta:
        model = Results
        fields = '__all__'