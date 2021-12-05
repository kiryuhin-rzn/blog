from django.db import models
from django.urls import reverse



class Lodging(models.Model):
    name = models.CharField(max_length=100, verbose_name='название', blank=True)
    lodging_type = models.ForeignKey('LodgingType', on_delete=models.CASCADE)#lodgigng
    numder = models.ForeignKey('NumberRooms', on_delete=models.CASCADE)
    description = models.TextField(verbose_name='описание', default='')
    published_at = models.DateTimeField(verbose_name='дата публикации', null=True)
    is_published = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('lodging_detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'жилище'
        verbose_name_plural = 'жилища'

    def __str__(self):
        return self.name


class LodgingType(models.Model):
    name = models.CharField(max_length=100, verbose_name='тип', blank=True)

    class Meta:
        verbose_name = 'тип жилища'
        verbose_name_plural = 'типы жилища'

    def __str__(self):
        return self.name


class NumberRooms(models.Model):
    number = models.PositiveIntegerField(blank=True, verbose_name='количество')
    numbers = models.CharField(max_length=100, blank=True, verbose_name='количество')

    class Meta:
        verbose_name = 'количество комнат'
        verbose_name_plural = 'количество комнат'

    def __str__(self):
        return self.numbers


class News(models.Model):
    title = models.CharField(max_length=1000, verbose_name='заголовок', blank=True)
    text = models.TextField(verbose_name='текст', blank=True)
    date_publication = models.DateTimeField(verbose_name='дата публикации', null=True)

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'

    def __str__(self):
        return self.title
