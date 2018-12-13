from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Hobby, Profile
from QMLove.forms import UserForm, ProfileForm
from .filters import ProfileFilter
from collections import *

def index(request):
    # exclude the admin, which has id number 1
    # retrieve all the users and hobbies
    users = User.objects.all().exclude(username='admin')
    hobbies = Hobby.objects.all()

    # if the user making the request is an admin,
    # show all the records
    if request.user.is_staff:
        return render(request, "QMLove/index.html", {'users': users, 'hobbies': hobbies})

    # only execute the below code if the user is authenticated
    if (request.user.is_authenticated):
        # get the profile of the current user
        # the current user is the user that makes a request to the index page
        currentUser = Profile.objects.get(user=request.user)

        # get all the users that have common interests with the current logged in user
        # exclude the current user
        related_users = Profile.objects.filter(hobby__in=currentUser.hobby.all()).exclude(id=currentUser.id)

        # related_users returns [<Profile: user1>, <Profile: user1>, <Profile: user2>]
        # that means, the current loggedin user has two common hobbies with user1, and one common hobby with user2
        # in order to find the users with the most hobbies in common, a Counter is used
        # the Counter returns [(<Profile: user1>, 2), (<Profile: user2>, 1)]
        related_users_sorted = Counter(related_users).most_common(10)
        # extracts the users from the counter
        # similar_interests stores user1, user2, etc.
        similar_interests = [user for user,count in related_users_sorted]

        return render(request, "QMLove/index.html", {'similar_interests': similar_interests, 'hobbies': hobbies})
    # if no user is authenticated, display all the users registered
    else:
        return render(request, "QMLove/index.html", {'users': users, 'hobbies': hobbies})

def register(request):
    if request.method == "POST":
        userForm = UserForm(data=request.POST)
        profileForm = ProfileForm(request.POST, request.FILES)
        if userForm.is_valid() and profileForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()

            # don't commit the profile to the db yet
            # the profile needs to be associated with the user and then saved
            profile = profileForm.save(commit=False)

            # if an image has been uploaded,
            # attach it to the user's profile
            if 'image' in request.FILES:
                profile.image = request.FILES['image']

            # associate the profile with the user
            # and save it to the db
            profile.user = user
            profile.save()

            # retrieve the indexes of hobbies selected
            # so they can be iterated over and added each to profile
            # getlist is used to retrieve the indexes of hobbies selected
            hobbies = request.POST.getlist('hobby')

            # for each hobby index
            # retrieve the hobby from the db using the index
            # and add the hobby to the profile
            for index in hobbies:
                profile.hobby.add(Hobby.objects.get(id=index))

            # log in the user after registration
            login(request, user)

            return redirect('/')
        else:
            return render(request, 'QMLove/register.html', {'userForm': userForm, 'profileForm': profileForm})
    else:
        userForm = UserForm()
        profileForm = ProfileForm()
        return render(request, 'QMLove/register.html', {'userForm': userForm, 'profileForm': profileForm})

# handle the filtering
def search(request):
    # get all the profiles except the profile of the current user logged in
    profiles = Profile.objects.all().exclude(user_id=request.user.id)
    # pass the request to the ProfileFilter and the profiles
    user_filter = ProfileFilter(request.GET, queryset=profiles)
    return render(request, 'QMLove/search.html', {'filter': user_filter})
