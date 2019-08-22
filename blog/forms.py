from django.contrib.auth.models import User
from django import forms
from . import models

class Signup(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password"]

class UserProfile(forms.ModelForm):
    # SEX_CHOICES= (
    #     ('M', 'Male'),
    #     ('F', 'Female')
    # )
    # sex = forms.CharField(widget=forms.Select(choices=SEX_CHOICES))
    class Meta:
        model = models.UserProfileInfo
        fields = ["profile_pic","dateOfBirth","sex"]
        # dateOfBirth = forms.DateField(
        #     widget = forms.DateInput(format='%m%d%Y', attrs={'class':'datepicker'}),
        #     input_formats=('%m%d%Y',)
        # )
        widgets = {
            'dateOfBirth': forms.DateInput(format='%m%d%Y', attrs={'class':'datepicker'}),
            'sex':forms.Select(attrs={'class':'select'})
        }