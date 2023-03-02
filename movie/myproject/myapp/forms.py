from django import forms
from . models import table

class tables_form(forms.ModelForm):
    class Meta:
        model = table
        fields = ['name','year','desc','image']