from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('', index_page, name='index'),
    path('profile', profile_page, name='profile'),
    path('forum', forum_page, name='forum'),
]