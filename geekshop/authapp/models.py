from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст')
