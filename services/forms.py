from django import forms
from django.forms import ModelForm, DateField
from django.contrib.auth.models import User
from .models import Service
from .models import Book


class Submit(forms.ModelForm):
   owner=forms.CharField(label='owner',required=True)
   pet_name = forms.CharField(label='pet_name',required=True)
   class Meta:
      model=Book
      fields = ['owner','services','pet_name','date','statuses']
      widgets = {'statuses': forms.HiddenInput()}


      # fields = '__all__'
      # widgets = {'statuses': forms.HiddenInput(),
      #            'services': forms.HiddenInput(),
      #            'owners': forms.HiddenInput()}