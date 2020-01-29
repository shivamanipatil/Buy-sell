from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


def user_directory_path(instance, filename):
    return 'uploads/user_{0}/{1}'.format(instance.user.id, filename)

class Product(models.Model):
    """Product model with seller as foreign key on user"""
    name =  models.CharField(max_length=30)
    description = models.TextField()
    age = models.FloatField()
    cost = models.FloatField()
    address = models.CharField(max_length=100)
    seller = models.ForeignKey(User, on_delete=models.CASCADE) 
    image1 = models.ImageField(upload_to='uploads/', null=True, blank=True)
    image2 = models.ImageField(upload_to='uploads/', null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    #function to return url string for displaying product after its creation
    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk':self.pk})

