from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'category',
                    'updated_at', 'is_published', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_editable = ('is_published', 'category')

    fields = ('title', 'content', 'category', 'is_published', 'photo',
              'get_photo', 'updated_at',  'created_at',  'views')

    readonly_fields = ('updated_at', 'created_at',  'get_photo', 'views')

    def get_photo(self, obj):
        if (obj.photo):
            return mark_safe(f"<img src='{obj.photo.url}' width='75'>")

    get_photo.short_description = 'Фото'


admin.site.register(News, NewsAdmin)
admin.site.register(Category)
