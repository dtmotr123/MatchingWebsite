from django.contrib.auth.models import User
from django.db import models

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

    hobby = models.CharField(choices=HOBBIES, max_length=1, null=True)

class Profile(models.Model):
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #profileImage = models.ImageField(upload_to='profile_images')
    email = models.EmailField(max_length=254, blank=True)
    gender = models.CharField(choices=GENDERS, max_length=1, null=True, default='')
    dob = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    hobby = models.ManyToManyField(Hobby)

    def __str__(self):
        return self.user.username
