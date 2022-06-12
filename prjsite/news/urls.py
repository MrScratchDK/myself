from django.urls import path
from .views import *


urlpatterns = [
    path('post_list/', main, name='main'),
    path('new/<str:slug>', post, name='post'),
    path('author_list/', AuthorList.as_view()),
    # path('post/<str:slug>', Post.as_view()),
    path('post_list_a/', PostList.as_view()),
    # path('post/<int:pk>/', Post.as_view()),
    # path('post_create/', PostCreate.as_view()),
]