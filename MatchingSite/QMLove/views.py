from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Hobby
from QMLove.forms import UserForm, ProfileForm

def index(request):
    users = User.objects.all().exclude(id=1)
    hobbies = Hobby.objects.all()

    return render(request, "QMLove/index.html", {'users': users, 'hobbies': hobbies})

def register(request):
    if request.method == "POST":
        userForm = UserForm(data=request.POST)
        profileForm = ProfileForm(request.POST, request.FILES)
        if userForm.is_valid() and profileForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()

            profile = profileForm.save(commit=False)

            # if an image has been uploaded,
            # attach it to the user's profile
            if 'image' in request.FILES:
                profile.image = request.FILES['image']

            profile.user = user
            profile.save()

            # retrieve the indexes of hobbies selected
            # so they can be iterated over and added to each profile
            # getlist is used to retrieve the indexes of hobbies selected
            hobbies = request.POST.getlist('hobby')

            # for each hobby index
            # add the hobby to the profile
            for index in hobbies:
                profile.hobby.add(Hobby.objects.get(id=index))

            return redirect('/')
        else:
            return render(request, 'QMLove/register.html', {'userForm': userForm, 'profileForm': profileForm})
    else:
        userForm = UserForm()
        profileForm = ProfileForm()
        return render(request, 'QMLove/register.html',{'userForm': userForm, 'profileForm': profileForm})
