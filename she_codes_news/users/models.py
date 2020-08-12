from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser (AbstractUser):
    dob = models.DateField(null=True, blank=True)
    bio = models.TextField(null=True)
    profile_picture = models.URLField(null=True, blank=True)
    # bio

    def __str__(self):
        return self.username