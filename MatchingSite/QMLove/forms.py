from django import forms
from QMLove.models import Profile
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = [
                  'user',
                  'password1', 
                  'email', 
                  'dob',
                 ]
        
form = RegisterForm()