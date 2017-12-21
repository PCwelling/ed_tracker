# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login.models import User
from ..people.models import Student
from ..course.models import Course
from .models import Instructor
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import InstructorForm

# Create your views here.

def logout(request):
    del request.session['user_id']
    return redirect('/')

def instructor_dashboard(request):
    if "user_id" not in request.session:
        return redirect ('/')

    context = {
        "user" : User.objects.get(id=request.session['user_id']),
        "instructors" : Instructor.objects.all(),
    }
    return render(request, 'instructor/instructor_dashboard.html', context)

def instructor_add(request):
    if "user_id" not in request.session:
        return redirect ('/')
    
    form = InstructorForm()

    context = {
        "instructorForm" : form
    }
    return render(request, 'instructor/instructor_create.html', context)

def instructor_create(request):
    if "user_id" not in request.session:
        return redirect ('/')

    if request.method == "POST":
        bound_form = InstructorForm(request.POST)
        if bound_form.is_valid():
            bound_form.save()
            print bound_form.is_valid()
            print bound_form.errors
        return redirect('/instructor')
   
    # if type(result) == list:
    #     for err in result:
    #         messages.error(request, err)
    #     return redirect('/people/student_create')
    # messages.success(request, "Successfully added a new student!")
    # return redirect('/people/studnet_dashboard')

def instructor_view(request, instructor_id):
    if "user_id" not in request.session:
        return redirect ('/')

    context = {
        "instructor" : Instructor.objects.get(id=instructor_id),
        "course" : Course.objects.filter(instructor__id=instructor_id)
    }
    return render(request, 'instructor/instructor_view.html', context)
    
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
	return render(request, 'instructor/instructor_create.html')