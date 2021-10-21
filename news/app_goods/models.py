from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=1000, blank=True, db_index=True, verbose_name='название')
    text = models.TextField()
    date_publication = models.DateField(auto_now_add=True)