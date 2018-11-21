from django import forms
from QMLove.models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    dob = forms.DateField(initial=datetime.date.today, widget=forms.widgets.DateInput(format="%m/%d/%Y"))
    
    class Meta:
        model = User
        fields = ('username', 
                  'first_name', 
                  'last_name', 
                  'dob',
                  'email', 
                  'password1', 
                  'password2',
                 )
        
        def save(self, commit=True):
            user = super(RegisterationForm, self).save(commit=False)
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.email = self.cleaned_data['email']
            user.dob = self.cleaner_data['dob']
        
            if commit:
                user.save()
   
            return user
        


