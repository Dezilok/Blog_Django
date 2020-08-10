from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField(default=0, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    about_me = models.TextField(default='About me')

    def __str__(self):
        return f'{self.user.username} Profile'
