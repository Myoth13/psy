from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import UpdateUserProfileForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context


# Create your views here.
@login_required
def profile_main(request, *args, **kwargs):
    #user = request.user._wrapped if hasattr(request.user, '_wrapped') else request.user
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


########### register here #####################################
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            ######################### mail system ####################################
            htmly = get_template('registration/Email.html')
            d = {'username': username}
            subject, from_email, to = 'welcome', 'your_email@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            ##################################################################
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form, 'title': 'register here'})

