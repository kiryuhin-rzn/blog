from django.db import models
from django.contrib.auth.models import User


class Shop(models.Model):
    name = models.CharField(max_length=200, db_index=True, blank=True)

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    def __str__(self):
        return self.name


class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete = models.CASCADE)
    name = models.CharField(max_length=200, db_index=True, blank=True)
    slug = models.SlugField(max_length=200, db_index=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    number = models.PositiveIntegerField()


    class Meta:
        #ordering = ('name',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продкуты'

    def __str__(self):
        return self.name


class CartProduct(models.Model):
    """ Объект корзины """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Покупатель')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(blank=True)
    final_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    def __str__(self):
        return self.product.name


class Cart(models.Model):
    """ Корзина """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Покупатель')
    product = models.ManyToManyField(CartProduct)#было ManyToManyField
    final_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True,)


class ReportSales(models.Model):
    """Отчет продаж"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    number = models.PositiveIntegerField(blank=True, null=True)
