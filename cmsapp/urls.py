from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogpost/<str:slug>', views.blogpost, name='blogpost'),
    path('create-post', views.create_post, name='create_post')
]