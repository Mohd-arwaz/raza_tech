from django.db import models

# Create your models here.

class student (models.Model):
    Name = models.CharField(max_length=50)
    age = models.IntegerField()
    fathers_name = models.CharField(max_length=200)
    Address= models.CharField(max_length=260)
    city = models.CharField(max_length=160,null=True,default='pilibhit')

   

