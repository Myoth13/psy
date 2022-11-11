from django.urls import path
from . import views


urlpatterns = [
    path('program', views.program_main, name='program_main'),
    path('program/<str:slug>', views.program_desc, name='program_desc'),
    path('create-program', views.program_create, name='program_create'),
    path('manage-program/<str:slug>', views.program_manage, name='program_manage'),
    path('delete-program/<str:slug>', views.program_delete, name='program_delete'),
    path('update-program/<str:slug>', views.program_update, name='program_update'),
]