from django.contrib import admin

from .models import *

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')

admin.site.register(News, NewsAdmin)
admin.site.register(Category)
