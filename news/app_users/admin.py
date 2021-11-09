from django.contrib import admin
from app_users.models import Profile, Account


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'telephone', 'verification', 'number_news')
    list_filter = ('verification', )

    actions = ['mark_as_verified', 'mark_as_unverified']

    def mark_as_verified(self, request, queryset):
        queryset.update(verification='verified')

    def mark_as_unverified(self, request, queryset):
        queryset.update(verification='unverified')

    mark_as_verified.short_description = 'Верифицирован'
    mark_as_unverified.short_description = 'Не верифицирован'

admin.site.register(Profile, ProfileAdmin)


class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance', 'promotions', 'offers', 'payment_history')

admin.site.register(Account, AccountAdmin)