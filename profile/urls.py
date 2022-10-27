from django.urls import path
from . import views


urlpatterns = [
    path('profile-main/', views.profile_main, name='profile_main'),
    path('profile-update/', views.profile_update, name='profile_update'),
    path('profile-delete/', views.profile_delete, name='profile_delete'),
    path("registration", views.register, name="registration"),
]
