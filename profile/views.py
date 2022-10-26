from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserProfile
from .forms import UpdateUserProfileForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required()
def profile_main(request):
    user_id = request.user
    user_profile = UserProfile.objects.get(user_id=user_id)
    context = {'profile': user_profile}
    return render(request, 'profile_main.html', context=context)


@login_required()
def profile_update(request):
    user_id = request.user
    user_profile = UserProfile.objects.get(user_id=user_id)
    form = UpdateUserProfileForm(instance=user_profile)

    if request.method == 'POST':
        form = UpdateUserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.info(request, 'Profile was updated successfully')
            return redirect('profile_main')

    context = {'form': form, 'profile': user_profile}
    return render(request, 'profile_update.html', context=context)

