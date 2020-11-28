
from django import forms
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm
from .forms import ContactForm


# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} created successfully.')
            return redirect('login')
    else:
        form = RegistrationForm()
        return render(request, 'users/register.html', {'form': form})


def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contactus')
    else:
        form = ContactForm()
        return render(request, 'portfoliodatabase/portfolio', {'form': form})
