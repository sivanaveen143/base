from email import message
from django.db import models

# Create your models here.
class chat(models.Model):
    username = models.CharField(max_length=20)
    message = models.CharField(max_length=100)