"""
Definition of views.
"""

from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .models import AccountInfo

def login_student(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Login As Student',
            'year':datetime.now().year,
        }
    )

def login_teacher(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Login As Teacher',
            'message':'Login As Teacher.',
            'year':datetime.now().year,
        }
    )

def signup_student(request):
    """Renders the about page."""
    print("sssss")

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'Signup As Teacher',
            'message':'Signup As Teacher',
            'year':datetime.now().year,
        }
    )
def signup_teacher(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/signup_teacher.html',
        {
            'title':'Signup as teacher',
            'message':'Signup as teacher',
            'year':datetime.now().year,
        }
    )
def add_student_form_submission(request):
    std_name = request.POST["student_name"]
    std_password = request.POST["student_password"]

    account_info.save()
    return render(request,'app/index.html')
