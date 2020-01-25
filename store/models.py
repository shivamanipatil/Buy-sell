from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name =  models.CharField(max_length=30)
    description = models.TextField()
    age = models.FloatField()
    cost = models.FloatField()
    address = models.CharField(max_length=100)
    seller = models.ForeignKey(User, on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.name