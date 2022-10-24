from django.urls import path
from . import views


urlpatterns = [
    path('profile-main/', views.profile_main, name='profile_main'),
]
