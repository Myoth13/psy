from django.db import models
import uuid

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=500)
    body = models.TextField()
    post_id = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='post/img')
    slug = models.SlugField()

    def __str__(self):
        return self.title
