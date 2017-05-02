from django.shortcuts import render, redirect
from .forms import *
from .models import *
# Create your views here.

def user_create(request):
    form = UserForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
    context = {
        "form": form,
        "heading": "Create a user",
    }

    return render(request, "user_create.html", context)

def attendance_create(request):
    form = AttendanceForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
    context = {
        "form": form,
        "heading": "Edit the attendance",
    }
    return render(request, "attendance_create.html", context)

def mark_create(request):

    form = MarkForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
    context = {
        "form": form,
        "heading": "Edit the marks",
    }
    return render(request, "mark_create.html", context)

def view_details(request):
    context = {
        'regNo': reg,
    }
    return render(request, "view.html", context)

def cio_view(request):
    context = {

    }
    if request.method=="POST":
        q = request.POST.get('query')
        q = q.split(' ')
        print q
        if q[0] == "view":
            regNo = str(q[2])
            userset = User.objects.filter(regNo=regNo)
            c = {
            'regNo': regNo,
            'userset': userset[0],
            }
            return render(request, "user_view.html", c)

        if q[0] == "generate":
            print "set to generate"


    return render(request, "cio.html", context)
