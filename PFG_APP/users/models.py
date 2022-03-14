from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .managers import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=100, unique=True)
    password = models.CharField(verbose_name="password", max_length=20)
    created_on = models.DateTimeField(verbose_name="created_on", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last_login", auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_professor = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = ['email']
    REQUIRED_FIELDS = ['email', 'password', ]

    objects = UserManager()

    def __str__(self):
        return self.email
