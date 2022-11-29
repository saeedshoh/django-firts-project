from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    # path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name='category_show'),
    path('post/<int:post_id>/', get_post, name='post_show'),
    path('create-news', add_news, name='news.create')
]
