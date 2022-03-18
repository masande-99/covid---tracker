<<<<<<< HEAD
from django.forms import ModelForm
from django import forms
from .models import *


class ResultsForm(ModelForm):
    class Meta:
        model = Results
=======
from django.forms import ModelForm
from django import forms
from .models import *


class ResultsForm(ModelForm):
    class Meta:
        model = Results
>>>>>>> a8c3a92c522314a3fd91ccb28064329db91097b3
        fields = '__all__'