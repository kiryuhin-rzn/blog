from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    VERIFICATION_CHOICES = (
    ('unverified', 'Unverified'),
    ('verified', 'Verified'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=36, blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    verification = models.CharField(max_length=20, choices=VERIFICATION_CHOICES, default='unverified')
    number_news = models.IntegerField(blank=True)

    class Meta:
        verbose_name = 'профиль'
        verbose_name_plural = 'профили'
        permissions = (
            ('can_verify', 'Может верифицировать'),
            )

'''
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.CharField(max_length=100)
    promotions = models.CharField(max_length=100)
    offers = models.CharField(max_length=100)
    payment_history = models.CharField(max_length=100)
'''