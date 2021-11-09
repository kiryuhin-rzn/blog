from django.contrib import admin
from app_goods.models import Item, Author, Book


# Create your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')

admin.site.register(Item, ItemAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'birthday')

admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'pages')

admin.site.register(Book, BookAdmin)
