from django import forms
from .models import *


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        exclude = [
            'is_active',
            'created',
            'updated',
        ]


class DoctorTimeForm(forms.ModelForm):
    class Meta:
        model = DoctorTime
        exclude = []


class DoctorExperienceForm(forms.ModelForm):
    class Meta:
        model = DoctorExperience
        exclude = []
