from django import forms
from QMLove.models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'gender', 'dob', 'hobby')

# class RegistrationForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#     dob = forms.DateField(initial=datetime.date.today, widget=forms.widgets.DateInput(format="%m/%d/%Y"))
#
#     GENDERS = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#     )
#     gender = forms.ChoiceField(widget=forms.Select,
#                                          choices=GENDERS)
#
#     class Meta:
#         model = User
#         fields = ('username',
#                   'first_name',
#                   'last_name',
#                   'dob',
#                   'gender',
#                   'email',
#                   'password1',
#                   'password2',
#                  )
#
#     ##This gets called in views.py by form.save()
#     def save(self, commit=True):
#         user = super(RegistrationForm, self).save(commit=False)
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         user.email = self.cleaned_data['email']
#         user.dob = self.cleaned_data['dob']
#         user.gender = self.cleaned_data['gender']
#
#
#         if commit: #TESTED and it does run after submitting form
#             user.save()
#
#         return user
