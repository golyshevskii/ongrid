from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomeManager(BaseUserManager):
    """custome manager for creating user and superuser"""

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('User must have an email')
        
        user = self.model(email=self.normalize_email(email))
        user.set_password(password=password)
        user.save()

        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save()
        return user


class CustomeUser(AbstractUser):
    """custome user model with email main username field"""

    email = models.CharField(max_length=255, unique=True, verbose_name='Email')
    name = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomeManager()

    def __str__(self):
        return self.email
