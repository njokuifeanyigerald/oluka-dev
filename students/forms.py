from django import forms
from .models import *


class WAECForm(forms.ModelForm):

    class Meta:
        model = WAEC
        fields = ['result','accept']
