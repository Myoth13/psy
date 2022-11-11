from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post
from .forms import PostForm
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.conf import settings
from program.models import Program


def index(request):
    posts = Post.objects.all().order_by('-created')[:3]
    programs = Program.objects.filter(is_active=True).order_by('-created')[:3]
    context = {'posts': posts, 'programs': programs}
    return render(request, 'index.html', context=context)


def bloghome(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog_home.html', context=context)


def blogpost(request, slug):
    post = Post.objects.get(slug=slug)
    posts = Post.objects.exclude(post_id__exact=post.post_id)[:5]
    context = {'post': post, 'posts': posts}
    return render(request, 'post_descr.html', context=context)


@login_required
def create_post(request):
    if request.user.has_perm('post.create_post'):
        form = PostForm
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.slug = slugify(post.title)
                post.author = request.user
                post.save()
                messages.info(request, 'Article was created successfully')
                return redirect('index')
        context = {'form': form}
        return render(request, 'post_create.html', context)
    else:
        return redirect('index')


@login_required
def update_post(request, slug):
    if request.user.has_perm('post.create_post'):
        post = Post.objects.get(slug=slug)
        if post.author == request.user:
            form = PostForm(instance=post)
            if request.method == 'POST':
                form = PostForm(request.POST, request.FILES, instance=post)
                if form.is_valid():
                    form.save()
                    messages.info(request, 'Article was updated successfully')
                    return redirect('blogpost', slug=post.slug)
            context = {'form': form}
            return render(request, 'post_create.html', context)
        else:
            return redirect('index')
    else:
        return redirect('index')


@login_required
def delete_post(request, slug):
    if request.user.has_perm('post.delete_post'):
        post = Post.objects.get(slug=slug)
        if post.author == request.user:
            form = PostForm(instance=post)
            if request.method == 'POST':
                post.delete()
                messages.info(request, 'Article was deleted successfully')
                return redirect('index')
            context = {'form': form}
            return render(request, 'post_delete.html', context)
        else:
            return redirect('index')
    else:
        return redirect('index')


def about(request):
    users = settings.AUTH_USER_MODEL.objects.filter(groups__name='Admins')
    print('!!!!!!!!!!!!!!!!!!!')
    exit()
    context = {'users': users}
    return render(request, 'about.html', context=context)


def contact(request):
    context = {}
    return render(request, 'contact.html', context=context)
