from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post
from .forms import PostForm
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from profile.models import UserProfile, User


# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'index.html', context=context)


def bloghome(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog_home.html', context=context)


def blogpost(request, slug):
    post = Post.objects.get(slug=slug)
    posts = Post.objects.exclude(post_id__exact=post.post_id)[:5]
    context = {'post': post, 'posts': posts}
    return render(request, 'blog_post.html', context=context)


@login_required
def create_post(request):
    if request.user.has_perm('post.create_post'):
        form = PostForm
        user_profile = User.objects.get(username=request.user)
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.slug = slugify(post.title)
                post.author = user_profile
                post.save()
                messages.info(request, 'Article was created successfully')
                return redirect('index')
        context = {'form': form}
        return render(request, 'create_post.html', context)
    else:
        return redirect('index')


@login_required
def update_post(request, slug):
    if request.user.has_perm('post.create_post'):
        user_profile = User.objects.get(username=request.user)
        post = Post.objects.get(slug=slug)
        if post.author == user_profile:
            form = PostForm(instance=post)
            if request.method == 'POST':
                form = PostForm(request.POST, request.FILES, instance=post)
                if form.is_valid():
                    form.save()
                    messages.info(request, 'Article was updated successfully')
                    return redirect('blogpost', slug=post.slug)
            context = {'form': form}
            return render(request, 'create_post.html', context)
        else:
            return redirect('index')
    else:
        return redirect('index')


@login_required
def delete_post(request, slug):
    if request.user.has_perm('post.delete_post'):
        user_profile = User.objects.get(username=request.user)
        post = Post.objects.get(slug=slug)
        if post.author == user_profile:
            form = PostForm(instance=post)
            if request.method == 'POST':
                post.delete()
                messages.info(request, 'Article was deleted successfully')
                return redirect('index')
            context = {'form': form}
            return render(request, 'delete_post.html', context)
        else:
            return redirect('index')
    else:
        return redirect('index')


def about(request):
    users = User.objects.filter(groups__name='Admins')
    context = {'users': users}
    return render(request, 'about.html', context=context)


def contact(request):
    context = {}
    return render(request, 'contact.html', context=context)
