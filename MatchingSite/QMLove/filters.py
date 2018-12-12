from django.contrib.auth.models import User
from .models import Hobby, Profile
import django_filters
from datetime import datetime

class ProfileFilter(django_filters.FilterSet):

    class Meta:
        model = Profile
        fields = {
            'gender': ['exact'],
            'dob': ['year__gt', 'year__lt'],
            'hobby': ['exact']
        }
