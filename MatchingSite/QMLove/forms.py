from django import forms
from QMLove.models import Profile, Hobby
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime
from datetime import date

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name')

class ProfileForm(forms.ModelForm):
    HOBBIES = [[hobby.id, hobby.name] for hobby in Hobby.objects.all()]
    dob = forms.DateField(widget = (forms.widgets.DateInput(format="%m/%d/%Y", attrs={'placeholder':'mm/dd/yyyy'})))
    
    def clean_dob(self):
        dobCheck = self.cleaned_data['dob']
        today = date.today()
        if (dobCheck.year + 18, dobCheck.month, dobCheck.day) > (today.year, today.month, today.day):
            raise forms.ValidationError('You must be at least 18 years old to register')
        return dobCheck
    
    image = forms.ImageField(required=False)
    hobby = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=HOBBIES)

    class Meta:
        model = Profile
        fields = ('image', 'email', 'gender', 'dob', 'hobby')
