from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from QMLove.forms import UserForm, ProfileForm

def index(request):
    return HttpResponse("Hello, world. You're at the index!")

def register(request):
    if request.method == "POST":
        userForm = UserForm(data=request.POST)
        profileForm = ProfileForm(data=request.POST)
        if userForm.is_valid() and profileForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()

            profile = profileForm.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('/')
        else:
            return render(request, 'QMLove/register.html', {'userForm': userForm, 'profileForm': profileForm})
    else:
        userForm = UserForm()
        profileForm = ProfileForm()
        return render(request, 'QMLove/register.html',{'userForm': userForm, 'profileForm': profileForm})
