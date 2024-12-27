from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    contact = models.CharField(max_length = 15)
    password = models.CharField(max_length = 20)
    image = models.CharField(max_length = 100)
