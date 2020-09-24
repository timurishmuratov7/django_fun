from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    name = forms.CharField('username', max_length=100)
    email = forms.EmailField()

    class Meta:
        model = User
	    fields = ["username", "email", "password1", "password2"]
