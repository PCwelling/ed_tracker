from django import forms
from django.forms import ModelForm
from .models import Instructor

class InstructorForm(ModelForm):
    class Meta:
        model = Instructor
        fields = '__all__'