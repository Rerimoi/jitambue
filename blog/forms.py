from django.contrib.auth.models import User
from django import forms
# from blog.models import Profile

class Signup(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password"]

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('profile_pic', 'birth_date', 'sex')