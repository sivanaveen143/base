from email.policy import default
from enum import unique
from tokenize import Number
from django.db import models
import datetime as time

# Create your models here.
class userdetail(models.Model):
    username =   models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=10, unique= True)
    email = models.EmailField(max_length=254, unique=True)
    register_at = models.DateTimeField(auto_now=False, auto_now_add=True)  #(default= time.datetime.now())
    updated_at = models.DateTimeField(auto_now=True)
    latitude = models.TextField()
    longitude = models.TextField()