from django import forms
from django.forms import ModelForm
from .models import Agency

class AgencyForm(ModelForm):
    class Meta:
        model = Agency
        fields = '__all__'