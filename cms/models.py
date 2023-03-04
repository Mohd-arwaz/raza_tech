from django.db import models

# Create your models here.
class Employes(models.Model):
    Name = models.CharField(max_length=50)
    Email=models.CharField(max_length=100)
    Massage=models.TextField(max_length=250)    
