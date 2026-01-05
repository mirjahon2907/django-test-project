from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
import os


# Talaba haqida ma'lumot
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=120 ,null=True, blank=True)
    bio = models.TextField(null=True)
    location = models.CharField(blank=True, max_length=300)
    profile_image = models.ImageField(upload_to='portfolio', blank=True, default='portfolio/empty.png')
    social_github = models.CharField(blank=True, max_length=300)
    social_telegram = models.CharField(blank=True, max_length=300)
    social_instagram = models.CharField(blank=True, max_length=300)
    social_youtube = models.CharField(blank=True, max_length=300)
    social_website = models.CharField(blank=True, max_length=300)
    created = models.DateField(auto_now_add=True)
    file = models.FileField(upload_to='files', null=True, default=None)
    video = models.FileField(upload_to='videos', null=True, default=None)
    audio = models.FileField(upload_to='audios', null=True, default=None)
    rezyume = models.FileField(upload_to='files', null=True)

    def __str__(self):
        return str(self.user)







