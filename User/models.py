from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    """manager for user profiles"""

    def create_user(self, mobile, first_name, last_name, password=None, **extra_fields):
        """Create new user profile"""
        if not mobile:
            raise ValueError("User must have Mobile Number")
        if not first_name:
            raise ValueError("User must have First Name")
        if not last_name:
            raise ValueError("User must have Last Name")

        user = self.model(mobile=mobile, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, mobile, first_name, last_name, password, **extra_fields):
        user = self.create_user(mobile=mobile, first_name=first_name, last_name=last_name, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=25, default="first_name", editable=True)
    last_name = models.CharField(max_length=25, default="last_name", editable=True)
    mobile = models.CharField(max_length=11, unique=True, default="09123456789", editable=True)
    avatar = models.ImageField(default="hello world", editable=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_first_name(self):
        return self.first_name

    def __str__(self):
        return self.first_name + ' ' + self.last_name
