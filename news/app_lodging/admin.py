from django.contrib import admin
from app_lodging.models import Lodging, LodgingType, NumberRooms, News

class LodgingAdmin(admin.ModelAdmin):
    list_display = ('name', 'lodging_type')

admin.site.register(Lodging, LodgingAdmin)


class LodgingTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)

admin.site.register(LodgingType, LodgingTypeAdmin)


class NumberRoomsAdmin(admin.ModelAdmin):
    list_display = ('numbers',)

admin.site.register(NumberRooms, NumberRoomsAdmin)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')

admin.site.register(News, NewsAdmin)
