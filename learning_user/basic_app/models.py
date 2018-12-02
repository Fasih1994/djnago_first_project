from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):

    #creating relation ship with Base User
    user = models.OneToOneField(User,on_delete = models.CASCADE,primary_key=True)

    #additional fields that User Does not have
    portfolio_link = models.URLField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username;
