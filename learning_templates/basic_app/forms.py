from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo


#base form inherting from model

class UserForm(forms.ModelForm):
    password = forms.CharField(max_length=15, widget=forms.PasswordInput())

    class Meta():
        model= User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    
    class Meta():
        model= UserProfileInfo
        fields = ('portfolio_site','profile_pic')






