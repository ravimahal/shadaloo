from django import forms
from . import models
from django.contrib.auth.models import User

class UserProfile(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['first_name', 'last_name', 'email'] 

class ExtendedProfile(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['word_expiry_days'] 
