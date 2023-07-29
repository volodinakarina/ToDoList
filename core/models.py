# from django.contrib.auth.models import AbstractUser
# from django.db import models
#
#
# class User(AbstractUser):
#     email = models.EmailField('email address', blank=True, null=True)
#     updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    REQUIRED_FIELDS = []
