# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login.models import User
from .models import Student
from ..course.models import Course
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentForm

# Create your views here.
def people_dashboard(request):
    context = {
        "user" : User.objects.get(id=request.session['user_id']),
    }
    return render(request, 'people/people_dashboard.html', context)

def logout(request):
    del request.session['user_id']
    return redirect('/')

def student_dashboard(request):
    if "user_id" not in request.session:
        return redirect ('/')

    context = {
        "user" : User.objects.get(id=request.session['user_id']),
        "students" : Student.objects.all(),
    }
    return render(request, 'people/student_dashboard.html', context)

def student_add(request):
    if "user_id" not in request.session:
        return redirect ('/')
    
    form = StudentForm()

    context = {
        "studentForm" : form
    }
    return render(request, 'people/student_create.html', context)

def student_create(request):
    if "user_id" not in request.session:
        return redirect ('/')

    if request.method == "POST":
        bound_form = StudentForm(request.POST)
        if bound_form.is_valid():
            bound_form.save()
            print bound_form.is_valid()
            print bound_form.errors
        return redirect('/people/student_dashboard')
   
    # if type(result) == list:
    #     for err in result:
    #         messages.error(request, err)
    #     return redirect('/people/student_create')
    # messages.success(request, "Successfully added a new student!")
    # return redirect('/people/studnet_dashboard')

def student_view(request, student_id):
    if "user_id" not in request.session:
        return redirect ('/')

    context = {
        "student" : Student.objects.get(id=student_id),
        "courses" : Course.objects.filter(student__id=student_id),
    }
    return render(request, 'people/student_view.html', context)
    
def make_messages(request):
    errors = [
        "First error",
        "Second error",
        "Third error",
    ]
    for error in errors:
    # The messages object has a number of tags (including error), and we can use this shorthand for those tags:
        messages.error(request, error)
    # the message object will be held until the next time a page is rendered.
        return redirect('show_errors')

def show_errors(request):
	return render(request, 'people/student_create.html')