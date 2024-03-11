from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Year23(models.Model):
    filename = models.CharField(max_length=20)
    author = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    inst = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f"Day {self.filename} by {self.author}"

class User(AbstractUser):
    image = models.URLField(max_length=200, blank=True)
    def __str__(self):
        return f"{self.username}"