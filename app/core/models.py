"""
Database models.
"""
import uuid
import os

# from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

# def recipe_image_file_path(instance, filename):
#     """Generate file path for new recipe image."""
#     ext = os.path.splittext(filename)[1]
#     filename = f'{uuid.uuid4()}{ext}'

#     return os.path.join('uploads', 'recipe', filename)


def logo_image_file_path(instance, filename):
    """Generate file path for new recipe image."""
    ext = os.path.splittext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'

    return os.path.join('uploads', 'logo', filename)


def signature_image_file_path(instance, filename):
    """Generate file path for new recipe image."""
    ext = os.path.splittext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'

    return os.path.join('uploads', 'signature', filename)


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    phone_number = models.PositiveIntegerField(default=0)
    license = models.CharField(default=0, max_length=50)
    signature = models.ImageField(null=True,
                                  upload_to=signature_image_file_path)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Company(models.Model):
    company_id = models.UUIDField(primary_key=True,
                                  default=uuid.uuid4,
                                  editable=False,
                                  unique=True
                                  )
    owner = models.CharField(max_length=30)
    owner_email = models.CharField(max_length=75)
    company_name = models.CharField(max_length=75)
    company_addr = models.CharField(max_length=255)
    phone_number = models.PositiveIntegerField(default=0)
    logo = models.ImageField(null=True, upload_to=logo_image_file_path)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.company_name

# class ReportDetails(models.Model):
#     """Recipe object."""
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#     )
#     title = models.CharField(max_length=255)
#     description = models.TextField(blank=True)
#     time_minutes = models.IntegerField()
#     price = models.DecimalField(max_digits=5, decimal_places=2)
#     link = models.CharField(max_length=255, blank=True)

#     def __str__(self):
#         return self.title
