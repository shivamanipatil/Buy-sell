from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wallet = models.PositiveIntegerField(default=5000)
    transactions = models.TextField(default="")

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
class Transaction(models.Model):
    item = models.TextField(default="")
    buyer = models.ForeignKey(User, related_name='transactions_as_buyer', on_delete=models.CASCADE)
    seller = models.ForeignKey(User, related_name='transactions_as_seller', on_delete=models.CASCADE)
    value = models.PositiveIntegerField()