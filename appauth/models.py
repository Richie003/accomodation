from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError
from django.conf import settings
from django.utils.timezone import now


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            password=password
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, first_name, last_name, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


# 
class User(AbstractBaseUser):
    objects = UserManager()
    email = models.EmailField(verbose_name='email address', max_length=255,unique=True)
    first_name = models.CharField(max_length=255, blank=False, default='', verbose_name='first name')
    last_name = models.CharField(max_length=255, blank=False, default='', verbose_name='last name')
    created = models.DateTimeField(default=now)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        # The user is identified by their first & last name
        full_name = '%s %s'%(self.first_name, self.last_name)
        return full_name

    def get_short_name(self):
        # The user is identified by their email address
        return self.last_name

    def __str__(self):  # __unicode__ on Python 2
        full_name = '%s %s'%(self.first_name, self.last_name)
        return full_name

    def has_perms(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        return self.staff

    @property
    def is_admin(self):
        """Is the user a admin member?"""
        return self.admin

    @property
    def is_active(self):
        """Is the user active?"""
        return self.active


class UserBio(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    tel = models.CharField(default='', null=True, blank=True, max_length=11)
    full_name = models.CharField(default='', blank=False, max_length=100)
    gender = models.CharField(default="Male", max_length=6)
    created = models.DateTimeField(auto_now_add=True, editable=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

