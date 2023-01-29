from django.db import models
from django.contrib.auth.models import User

# Create your models here
# class User(models.Model):
#     username = models.CharField(max_length=264)

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #additional(classes)

    portfolio_site = models.URLField(blank=True)

    profile_pics = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
