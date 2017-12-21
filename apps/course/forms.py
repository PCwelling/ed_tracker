from django import forms
from django.forms import ModelForm
from .models import Course_type
from .models import Course

class Course_typeForm(ModelForm):
    class Meta:
        model = Course_type
        fields = '__all__'


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'