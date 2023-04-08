from django import forms
from .models import Book

class Submit(forms.ModelForm):
   owner=forms.CharField(label='Your Name',required=True)
   pet_name = forms.CharField(label="Pet's Name",required=True)
   class Meta:
      model=Book
      fields = ['owner','services','pet_name','animal','date','statuses']
      widgets = {'statuses': forms.HiddenInput(),
                 'services':forms.HiddenInput()}