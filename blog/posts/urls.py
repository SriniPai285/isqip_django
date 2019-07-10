from django.conf.urls import url
from django.urls import path
from posts.views import posts_list

urlpatterns = [
    url('^$', posts_list, name='posts_list'),
]