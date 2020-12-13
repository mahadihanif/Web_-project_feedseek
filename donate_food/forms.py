from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import SelectDateWidget
from .models import *




class DonatePostForm(forms.ModelForm):
    date = forms.DateField()
    
    class Meta:
        model = DonatePost
        fields = ['food_name','organization_name','how_many_people','date','location','add_note',]
        widgets = {
            'date': forms.widgets.SelectDateWidget()
        }