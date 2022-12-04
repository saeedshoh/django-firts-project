from django.contrib import admin

from .models import *

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'category', 'updated_at', 'is_published', 'views')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published', 'views', 'category')
    

admin.site.register(News, NewsAdmin)
admin.site.register(Category)
