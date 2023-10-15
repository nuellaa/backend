from django.db import models

# Create your models here.
class user(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    age = models.IntegerField(default=18)
   
   