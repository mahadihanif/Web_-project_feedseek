from django import forms
from phonenumber_field.formfields import PhoneNumberField
#from phone_field import PhoneField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    phone = PhoneNumberField()
    #phone_number = PhoneField()
    class Meta:
        model = Profile
        fields = ['full_name', 'address', 'phone', 'image', ]