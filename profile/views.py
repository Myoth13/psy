from django.shortcuts import render
from .models import UserProfile


# Create your views here.
def profile_main(request):
    user_id = request.user
    user_profile = UserProfile.objects.get(user_id=user_id)
    context = {'profile': user_profile}
    return render(request, 'profile_main.html', context=context)
