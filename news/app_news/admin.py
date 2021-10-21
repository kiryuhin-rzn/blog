from django.contrib import admin
from app_news.models import News, Comment, Tag, File


class TabularInlineComment(admin.TabularInline):
    model=Comment


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_publication', 'date_updated', 'status')
    list_filter = ('status', 'tag')
    inlines=[TabularInlineComment, ]

    actions = ['mark_as_published', 'mark_as_draft']

    def mark_as_published(self, request, queryset):
        queryset.update(status='published')

    def mark_as_draft(self, request, queryset):
        queryset.update(status='draft')

    mark_as_published.short_description = 'Перевести в статус Опубликовано'
    mark_as_draft.short_description = 'Перевести в статус Черновик'



class CommentAdmin(admin.ModelAdmin):
    list_display = ('news', 'author', 'get_text', 'status', 'user')
    list_filter = ('author', )

    def get_text(self, obj):
        if len(obj.text)<15:
            return obj.text
        else:
            return obj.text[0:15] + '...'

    def dell_text(self, request, queryset):
        queryset.update(text='Удалено администартором')


    actions = ['mark_as_p', 'mark_as_d', 'dell_text']

    def mark_as_p(self, request, queryset):
        queryset.update(status='p')

    def mark_as_d(self, request, queryset):
        queryset.update(status='d')


    dell_text.short_description = 'Удалено администратором'
    mark_as_p.short_description = 'Перевести в статус Опубликовано'
    mark_as_d.short_description = 'Перевести в статус Удалено администратором'


class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)
    #list_filter = ('title', )

class FileAdmin(admin.ModelAdmin):
    list_display = ('file', 'description',)


admin.site.register(News, NewsAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(File, FileAdmin)


