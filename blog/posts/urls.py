from django.conf.urls import url
from django.urls import path
from posts.views import posts_list
from posts.views import post_detail
from posts.views import new_post

urlpatterns = [
    url('^$', posts_list, name='posts_list'),
    path('posts/<int:pk>/', post_detail, name='post_detail'),
    path('posts/new/', new_post, name='post_new')
]