from django import forms
from .models import contact

class ContactForm(forms.ModelForm):
    class meta:
        model = contact
        fields = ['name', 'email', 'message']
       