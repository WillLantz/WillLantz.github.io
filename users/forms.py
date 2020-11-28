from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ContactUs


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['Name', 'Email', 'Comment']

        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control'}),
            'Comment': forms.TextInput(attrs={'class': 'form-control'}),
        }
