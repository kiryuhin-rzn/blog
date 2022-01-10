from django.contrib import admin
from app_todo.models import TodoListItem


class TodoListItemAdmin(admin.ModelAdmin):
    list_display = ('content', 'date_due')


admin.site.register(TodoListItem, TodoListItemAdmin)
