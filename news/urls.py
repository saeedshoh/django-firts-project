from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', NewsBycategory.as_view(), name='category_show'),
    path('news/<int:news_id>/',GetPostView.as_view(), name='post_show'),
    path('create-news', add_news, name='news.create'),
    path('tests', TestBaseView.as_view())
]
