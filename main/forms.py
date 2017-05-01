from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'regNo',
            'name',
            'sex',
            'dob',
            'department',
            'usertype',
            'phoneNo',
        ]

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = [
            'regNo',
            'term1',
            'term2',
        ]

class MarkForm(forms.ModelForm):
    class Meta:
        model = Mark
        fields = [
            'regNo',
            'sub1',
            'sub2',
            'sub3',
            'sub4',
            'sub5',
            'sub6'
        ]
