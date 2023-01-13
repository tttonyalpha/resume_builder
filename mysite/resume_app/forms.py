from django import forms
from .models import Resume
from django.contrib.auth.models import User
from django.forms import ModelForm


class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = ['name', 'surname', 'email', 'phone_number', 'college', 'pic']
