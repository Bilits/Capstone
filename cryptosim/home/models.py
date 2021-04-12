from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from home.price import *

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)
    postal_code = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=120, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    dob = models.DateField(blank=True, null=True)
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
    # balance = models.FloatField(null=True, default=0)
    # usdt = models.FloatField(null=True, default=0)
    # btc = models.FloatField(null=True, default=0)
    # eth = models.FloatField(null=True, default=0)
    # xrp = models.FloatField(null=True, default=0)
    # doge = models.FloatField(null=True, default=0)
    # brd = models.FloatField(null=True, default=0)
    # mkr = models.FloatField(null=True, default=0)
    # yfi = models.FloatField(null=True, default=0)
    # ont = models.FloatField(null=True, default=0)
    # rsr = models.FloatField(null=True, default=0)

    # def save(self, *args, **kwargs):
    #     self.tether = round(self.tether, 2)
    #     super(Wallet, self).save(*args, **kwargs)

    # def __str__(self):
    #     return str(self.profile)

    # def get_balance(self):
    #     return self.tether

    # def get_total(self):
    #     total = (get_btc()['price'] * self.bitcoin) + self.tether
    #     return total
        
@receiver(post_save, sender=Profile)
def wallet_creation(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(profile=instance)
    instance.wallet.save()


class Coin(models.Model):
    name = models.CharField(max_length=6, default='hi')
    price = models.FloatField(null=True, default=0)
    def __str__(self):
        return str(self.name)

class CoinInWallet(models.Model):
    amount = models.FloatField(null=True, default=0)
    wallet = models.ForeignKey('Wallet', on_delete=models.CASCADE)
    coin = models.ForeignKey('Coin', on_delete=models.CASCADE)


class Transaction(models.Model):
    wallet = models.ForeignKey('Wallet', on_delete=models.CASCADE)
    sellcoin = models.ForeignKey('Coin', on_delete=models.CASCADE)
    buycoin = models.ForeignKey('Coin', on_delete=models.CASCADE)
    amount = models.FloatField(null=True, default=0)