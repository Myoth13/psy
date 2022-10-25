from django.shortcuts import render
from .models import UserProfile
from .forms import UpdateUserProfileForm


# Create your views here.
def profile_main(request):
    user_id = request.user
    user_profile = UserProfile.objects.get(user_id=user_id)
    context = {'profile': user_profile}
    return render(request, 'profile_main.html', context=context)


def profile_update(request):
    user_id = request.user
    user_profile = UserProfile.objects.get(user_id=user_id)
    form = UpdateUserProfileForm(instance=user_profile)
    context = {'form': form}
    return render(request, 'profile_update.html', context=context)

