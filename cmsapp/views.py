from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.utils.text import slugify


# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'index.html', context=context)


def blogpost(request, slug):
    post = Post.objects.get(slug=slug)
    posts = Post.objects.exclude(post_id__exact=post.post_id)[:5]
    context = {'post': post, 'posts': posts}
    return render(request, 'blog_post.html', context=context)


def create_post(request):
    form = PostForm
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(post.title)
            post.save()
            return redirect('index')
    context = {'form': form}
    return render(request, 'create_post.html', context)
