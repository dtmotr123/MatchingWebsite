from django.contrib.auth.models import User
from django.db import models
from multiselectfield import MultiSelectField

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    #profileImage = models.ImageField(upload_to='profile_images')
    email = models.EmailField(max_length=254, blank=True)
    gender = models.CharField(max_length=6, blank=True)
    dob = models.DateField(auto_now=False, auto_now_add=False, blank=True)

    def __str__(self):
        return self.user.username

class Hobby(models.Model):
    HOBBIES = (
        ('1', 'Skiing'),
        ('2', 'Fishing'),
        ('3', 'Hunting'),
        ('4', 'Golf'),
        ('5', 'Reading'),
        ('6', 'Football'),
        ('7', 'Automobiles'),
        ('8', 'Fitness'),
        ('9', 'Politics'),
        ('10', 'Fashion'),
        ('11', 'Art')
    )
    hobby_name = MultiSelectField(choices=HOBBIES, null=True)
    users = models.ManyToManyField(Profile)

    def __str__(self):
        return str(self.user)
