from django.urls import path
from .views import *

urlpatterns = [
    path('', test, name='test'),
    path('rubrik/<int:pk>', get_rubrik, name='rubrik')
]
