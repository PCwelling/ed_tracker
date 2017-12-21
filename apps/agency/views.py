# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login.models import User
from .models import Agency
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AgencyForm

# Create your views here.

def logout(request):
    del request.session['user_id']
    return redirect('/')

def agency_dashboard(request):
    if "user_id" not in request.session:
        return redirect ('/')

    context = {
        "user" : User.objects.get(id=request.session['user_id']),
        "agencys" : Agency.objects.all(),
    }
    return render(request, 'agency/agency_dashboard.html', context)

def agency_add(request):
    if "user_id" not in request.session:
        return redirect ('/')
    
    form = AgencyForm()

    context = {
        "agencyForm" : form
    }
    return render(request, 'agency/agency_create.html', context)

def agency_create(request):
    if "user_id" not in request.session:
        return redirect ('/')

    if request.method == "POST":
        bound_form = AgencyForm(request.POST)
        if bound_form.is_valid():
            bound_form.save()
            print bound_form.is_valid()
            print bound_form.errors
        return redirect('/agency')
   
    # if type(result) == list:
    #     for err in result:
    #         messages.error(request, err)
    #     return redirect('/people/student_create')
    # messages.success(request, "Successfully added a new student!")
    # return redirect('/people/studnet_dashboard')

def agency_view(request, agency_id):
    if "user_id" not in request.session:
        return redirect ('/')

    context = {
        "agency" : Agency.objects.get(id = agency_id),
    }
    return render(request, 'agency/agency_view.html', context)
    
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
	return render(request, 'iagency/agency_create.html')