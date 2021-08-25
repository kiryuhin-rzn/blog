from django.contrib import admin
from app_news.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass
