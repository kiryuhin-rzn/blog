from django.contrib import admin
from app_goods.models import Item


# Create your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')

admin.site.register(Item, ItemAdmin)