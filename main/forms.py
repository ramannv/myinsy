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
            'en14401',
            'en14402',
            'en14403',
            'en14404',
            'en14405',
            'en14406',
        ]
