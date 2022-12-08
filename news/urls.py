from django.urls import path
from .views import *

urlpatterns = [
    path('test/', test, name='test'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', NewsBycategory.as_view(), name='category_show'),
    path('news/<int:news_id>/',GetPostView.as_view(), name='post_show'),
    path('create-news', add_news, name='news.create'),
    path('tests', TestBaseView.as_view())
]
