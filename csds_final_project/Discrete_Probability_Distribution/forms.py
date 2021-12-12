from django import forms
from django.forms import fields

from .models import TableValues

class InputX(forms.ModelForm):
    class Meta:
        model = TableValues
        fields = ['xValue']
