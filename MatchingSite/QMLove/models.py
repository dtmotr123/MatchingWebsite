from django.contrib.auth.models import User
from django.db import models

class Hobby(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Profile(models.Model):
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images')
    email = models.EmailField(max_length=254)
    gender = models.CharField(choices=GENDERS, max_length=1)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    hobby = models.ManyToManyField(Hobby)

    def __str__(self):
        return self.user.username
