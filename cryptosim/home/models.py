from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)
    beginner = models.BooleanField(default=False)
    professional = models.BooleanField(default=False)
    signup_confirmation = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Wallet(models.Model):
    profile = models.OneToOneField('Profile', on_delete=models.CASCADE, null=True)
    tether = models.FloatField(null=True, default=0)
    bitcoin = models.IntegerField(null=True, default=0)
    ethereum = models.IntegerField(null=True, default=0)
    ripple = models.IntegerField(null=True, default=0)

    def __str__(self):
        return str(self.profile)

    def get_balance(self):
        return self.tether

    def get_total(self):
        return self.tether

        
@receiver(post_save, sender=Profile)
def wallet_creation(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(profile=instance)
    instance.wallet.save()