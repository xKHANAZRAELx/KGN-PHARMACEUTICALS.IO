from django.forms import ModelForm
from .models.alogin import Alogin
from django import forms

class LoginForm(forms.ModelForm):
    class Meta:
        model=Alogin
        fields='__all__'
