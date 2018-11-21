from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from QMLove.forms import RegistrationForm



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def register(request):
    if request.method =="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/base.html')
    else:
        form = RegistrationForm()
        return render(request, 'QMLove/register.html',{'form':form})
   



            
            