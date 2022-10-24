from django.shortcuts import render
from .models import UserProfile


# Create your views here.
def profile_main(request):
    context = {}
    return render(request, 'profile_main.html', context=context)
