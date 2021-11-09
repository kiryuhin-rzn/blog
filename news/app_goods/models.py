from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=1000, blank=True, db_index=True, verbose_name='название')
    text = models.TextField()
    date_publication = models.DateField(auto_now_add=True)


class Author(models.Model):
    """Модель автора."""
    name = models.CharField(max_length=100, blank=True, verbose_name='name')
    surname = models.CharField(max_length=100, blank=True, verbose_name='surname')
    birthday = models.DateField(blank=True, verbose_name='birthday')

    def __str__(self):
        return f'{self.name}, {self.surname}'


class Book(models.Model):
    """Модель книги."""
    author = models.ForeignKey(Author, on_delete = models.CASCADE, null=True)#убрал null=True
    title = models.CharField(max_length=100, blank=True, verbose_name='title')
    isbn  = models.CharField(max_length=100, blank=True, verbose_name='isbn')
    release = models.DateField(blank=True, verbose_name='release')
    pages = models.CharField(max_length=100, blank=True, verbose_name='pages')
