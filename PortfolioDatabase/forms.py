from django import forms
from .models import Portfolio
from .models import ContactUs


class PortForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['port_name', 'port_desc', 'port_image', 'port_website']


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['Name', 'Email', 'Comment']

        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control'}),
            'Comment': forms.TextInput(attrs={'class': 'form-control'}),
        }
