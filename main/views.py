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
