from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from study_buddy.members.managers import AppUserManager


# Create your models here.

class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    objects = AppUserManager()

    USERNAME_FIELD = 'email'


class Profile(models.Model):
    """
    If we want eventually to have first_name and last_name,
    We have to do it in a separate class => in this case we use Profile class
    """
    first_name = models.CharField(max_length=100, )
    last_name = models.CharField(max_length=100, )
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE, primary_key=True,)

