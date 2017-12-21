# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login.models import User
from ..people.models import Student
from ..instructor.models import Instructor
from ..store.models import Store
from ..agency.models import Agency
from .models import Course, Course_type
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import Course_typeForm
from .forms import CourseForm


# Create your views here.

def logout(request):
    del request.session['user_id']
    return redirect('/')

def course_dashboard(request):
    context = {
        "user" : User.objects.get(id=request.session['user_id']),
    }
    return render(request, 'course/course_dashboard.html', context)

def course_type_add(request):
    if "user_id" not in request.session:
        return redirect ('/')
    
    form = Course_typeForm()

    context = {
        "course_types" : Course_type.objects.all(),
        "course_typeForm" : form
    }
    return render(request, 'course/course_type_create.html', context)

def course_type_create(request):
    if "user_id" not in request.session:
        return redirect ('/')

    if request.method == "POST":
        bound_form = Course_typeForm(request.POST)
        if bound_form.is_valid():
            bound_form.save()
            print bound_form.is_valid()
            print bound_form.errors
        return redirect('/course/')

def course_type_view(request, course_type_id):
    if "user_id" not in request.session:
        return redirect ('/')

    context = {
        "course_type" : Course_type.objects.get(id=course_type_id),
    }
    return render(request, 'course/course_type_view.html', context)

def course_add(request):
    if "user_id" not in request.session:
        return redirect ('/')
    
    form = CourseForm()

    context = {
        "courses" : Course.objects.all(),
        "courseForm" : form
    }
    return render(request, 'course/course_create.html', context)

def course_create(request):
    if "user_id" not in request.session:
        return redirect ('/')

    if request.method == "POST":
        bound_form = CourseForm(request.POST)
        if bound_form.is_valid():
            bound_form.save()
            print bound_form.is_valid()
            print bound_form.errors
        return redirect('/course/')

def course_view(request, course_id):
    if "user_id" not in request.session:
        return redirect ('/')

    u = Course.objects.get(id=course_id)
    students = u.student.all()
    instructors = u.instructor.all()

    context = {
        "course" : Course.objects.get(id=course_id),
        "allstudents" : Student.objects.exclude(courses__student=students),
        "students" : students,
        "instructors" : instructors,
    }
    return render(request, 'course/course_view.html', context)

    
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
	return render(request, 'course/course_create.html')

def remove_from_course(request):
    result = Course.objects.remove_from_course(request.POST)
    strurl = "/course/{}/course_view".format(request.POST['course_id'])
    return redirect(strurl)

def add_to_course(request):
    result = Course.objects.add_to_course(request.POST)
    strurl = "/course/{}/course_view".format(request.POST['course_id'])
    return redirect(strurl)