from django.shortcuts import render, redirect
from .models import UserProfile, User
from cmsapp.models import Post
from program.models import Program
from .forms import UpdateUserProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def profile_main(request, *args, **kwargs):
    #user_id = request.user
    #user_profile = UserProfile.objects.get(user_id=user_id)
    user_profile = request.user.userprofile
    posts = request.user.post_set.all
    programs = request.user.program_set.all
    context = {'profile': user_profile, 'posts': posts, 'programs': programs}
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


@login_required()
def profile_delete(request):
    user_id = request.user
    user_profile = UserProfile.objects.get(user_id=user_id)
    form = UpdateUserProfileForm(instance=user_profile)

    if request.method == 'POST':
        user_profile.delete()
        messages.info(request, 'Profile was deleted successfully')
        return redirect('logout')

    context = {'form': form, 'profile': user_profile}
    return render(request, 'profile_delete.html', context=context)
