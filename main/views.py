from django.shortcuts import render
from .forms import *
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
        'regNo': 'regNo',
    }
    return render(request, "view.html", context)

def cio_view(request):
    context = {

    }
    if request.method=="POST":
        q = request.POST.get('query')
        q = q.split(' ')
        print q[0]
        if q[0] == "view":
            regNo = q[2]

        if q[0] == "generate":
            print "set to generate"


    return render(request, "cio.html", context)
