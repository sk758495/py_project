from django.db import models

# Create your models here.

class student(models.Model):
    roll= models.CharField(max_length=100)
    name=models.CharField(max_length=50)
    email = models.EmailField(null=False, blank=False)
    address = models.CharField(max_length=255, null=False, blank=False)
    phone=models.CharField(max_length=10)
