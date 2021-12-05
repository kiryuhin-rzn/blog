from django.db import models
from django.contrib.auth.models import User
#from django.db.models.signals import post_save
#from django.dispatch import receiver
#from django.core.cache import cache
#from django.core.cache.utils import make_template_fragment_key


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


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.CharField(max_length=100, blank=True)#models.DecimalField(max_digits=10, decimal_places=2)
    promotions = models.CharField(max_length=100, blank=True)
    offers = models.CharField(max_length=100, blank=True)
    payment_history = models.CharField(max_length=100, blank=True)
    status = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=1)


'''
@receiver(post_save, sender=Account)
def clear_cache(sender, instance, **kwargs):
    key = make_template_fragment_key('footer', request.user.username)
    cache.delete(key)
'''
