import email
from email.policy import default
import imp
from operator import mod
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
# Create your models here.
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profile"""
    def create_user(self,email,name,password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')
        email=self.normalize_email(email)
        user=self.model(email=email,name=name)

        user.set_password(password)#encryption
        user.save(using=self._db)

        return user
    
    def create_superuser(self,email,name,password):
        """create and save a new superuser with given details"""
        user=self.create_user(email,name,password)

        user.is_superuser=True #automatically created by the PermissionMixin
        user.is_staff=True
        return user



class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)#users profile is active or not
    is_staff=models.BooleanField(default=False)
    #profile_pic=models.ImageField(default="default.jpg")

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=['name']

    def get_full_name(self):
        """Retreive fullname of the user"""
        return self.name

    def get_short_name(self):
        """Retreive short name"""
        return self.name

    def __str__(self):
        return self.email
