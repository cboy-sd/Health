from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    Permission,
    PermissionsMixin,
)
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(
            self, email, password=None, is_staff=False, is_active=True, **extra_fields
    ):
        """Create a user instance with the given email and password."""
        email = UserManager.normalize_email(email)
        # Google OAuth2 backend send unnecessary username field
        extra_fields.pop("username", None)

        user = self.model(
            email=email, is_active=is_active, is_staff=is_staff, **extra_fields
        )
        if password:
            user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        return self.create_user(
            email, password, is_staff=True, is_superuser=True, **extra_fields
        )

    def staff(self):
        return self.get_queryset().filter(is_staff=True)


class User(PermissionsMixin, AbstractBaseUser):
    GENDER = (
        ('u', 'Undefined'),
        ('m', 'Male'),
        ('f', 'Female'),
    )
    email = models.EmailField(unique=True)
    profile = models.ImageField(upload_to="user/profile", null=True, blank=True)
    full_name = models.CharField(max_length=256, blank=True)
    phone_number = models.CharField(max_length=13, blank=True)
    phone_number_2 = models.CharField(max_length=13, blank=True, null=True)
    gender = models.CharField(max_length=1, default='u', choices=GENDER)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_blacklisted = models.BooleanField(default=True)
    note = models.TextField(null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"

    objects = UserManager()

    def get_short_name(self):
        return self.email
