from django.db import models

# Create your models here.
class Example(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField


class Signup(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)

    
    