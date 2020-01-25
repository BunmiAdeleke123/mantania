from django.db import models

# Create your models here.

class Business(models.Model):
    Name= models.CharField(max_length=50)