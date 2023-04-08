from django import forms
from .models import Default_value
from django.contrib.auth.models import User
from services.models import Book

class Save(forms.ModelForm):
    name=forms.CharField(label='Your Name',required=True)
    pet_name = forms.CharField(label="Pet's Name",required=True)
    class Meta:
        model=Default_value
        fields = ['name','pet_name']

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control','cols': 10, 'rows': 20}))
    class Meta:
        model = User
        fields = ['email']

class UpdateStatus(forms.ModelForm):
    class Meta:
        model=Book
        fields=['statuses']
