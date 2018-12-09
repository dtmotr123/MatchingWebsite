from django import forms
from QMLove.models import Profile, Hobby
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name')

class ProfileForm(forms.ModelForm):
    HOBBIES = [[hobby.id, hobby.name] for hobby in Hobby.objects.all()]
    dob = forms.DateField(widget = (forms.widgets.DateInput(format="%d/%m/%Y", attrs={'placeholder':'dd/mm/yyyy'})))
    image = forms.ImageField(required=False)
    hobby = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=HOBBIES)

    class Meta:
        model = Profile
        fields = ('image', 'email', 'gender', 'dob', 'hobby')
