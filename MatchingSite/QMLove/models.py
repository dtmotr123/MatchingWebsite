from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #profileImage = models.ImageField(upload_to='profile_images')
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    gender = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    dob = models.DateField(auto_now=False, auto_now_add=False, blank=True)

    def __str__(self):
        return self.name

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Hobby(models.Model):
    hobby_name = (
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
    user = models.ManyToManyField(Profile)

    def __str__(self):
        return self.hobby_name
