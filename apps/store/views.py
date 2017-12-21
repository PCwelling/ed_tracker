# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login.models import User
from ..people.models import Student
from ..instructor.models import Instructor
from .models import Store
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StoreForm

# Create your views here.

def logout(request):
    del request.session['user_id']
    return redirect('/')

def store_dashboard(request):
    if "user_id" not in request.session:
        return redirect ('/')

    context = {
        "user" : User.objects.get(id=request.session['user_id']),
        "stores" : Store.objects.all(),
    }
    return render(request, 'store/store_dashboard.html', context)

def store_add(request):
    if "user_id" not in request.session:
        return redirect ('/')
    
    form = StoreForm()

    context = {
        "storeForm" : form
    }
    return render(request, 'store/store_create.html', context)

def store_create(request):
    if "user_id" not in request.session:
        return redirect ('/')

    if request.method == "POST":
        bound_form = StoreForm(request.POST)
        if bound_form.is_valid():
            bound_form.save()
            print bound_form.is_valid()
            print bound_form.errors
        return redirect('/store')
   

def store_view(request, store_id):
    if "user_id" not in request.session:
        return redirect ('/')

    context = {
        "store" : Store.objects.get(id= store_id),
    }
    return render(request, 'store/store_view.html', context)
    
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
	return render(request, 'store/store_create.html')