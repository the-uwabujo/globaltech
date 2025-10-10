from django.db import models

# Create your models here.

class Account(models.Model):
      email = models.EmailField(unique=True, max_length=50)
      name = models.CharField(max_length=255)