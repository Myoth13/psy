from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
import uuid


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=500)
    body = RichTextField()
    post_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='post/img')
    slug = models.SlugField(unique=True)
    category = models.ForeignKey('PostCategory', on_delete=models.SET_NULL, blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


class PostCategory(models.Model):
    title = models.CharField(max_length=100)
    category_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    slug = models.SlugField()

    def __str__(self):
        return self.title

