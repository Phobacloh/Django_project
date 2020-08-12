from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser (AbstractUser):
    # date of birth = models.DateField()
    # bio = models.TextField(null=True)
    # profile picture
    # bio

    def __str__(self):
        return self.username