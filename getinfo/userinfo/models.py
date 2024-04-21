from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from .managers import CustomUserManager


class User(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    dob = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=100, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class EducationalInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='educational_info')
    degree = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    graduation_year = models.IntegerField()
    subject = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15, blank=True, help_text="Enter your mobile number.")

    def __str__(self):
        return f"{self.user.email} - {self.degree} at {self.university}"