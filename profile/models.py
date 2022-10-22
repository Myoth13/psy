from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField
    username = models.CharField(max_length=200)
    occupation = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='profile/img', blank=True, null=True)
    about = models.TextField(max_length=2000)
    profile_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    def __str__(self):
        return self.username
