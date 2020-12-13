from django import forms
from .models import Post



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_choice','food_name', 'organization_name','how_many_people',
            'date', 'location', 'add_note']
        widgets = {
            'food_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Rice, Egg'}),
            'organization_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':' ABC Organization or Restaurant'}),
            'location': forms.TextInput(attrs={'class':'form-control', 'placeholder':' location where you want to donate'}),
            'date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'add_note': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Additional note'}),
        }