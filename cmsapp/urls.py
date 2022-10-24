from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('blogpost/<str:slug>', views.blogpost, name='blogpost'),
    path('blog-home', views.bloghome, name='bloghome'),
    path('create-post', views.create_post, name='create_post'),
    path('update-post/<str:slug>', views.update_post, name='update_post'),
    path('delete-post/<str:slug>', views.delete_post, name='delete_post'),
]
