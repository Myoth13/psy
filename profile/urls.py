from django.urls import path
from . import views


urlpatterns = [
    path('profile-main/<str:user_id>', views.profile_main, name='profile_main'),
]
