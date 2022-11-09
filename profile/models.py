from django.db import models
import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import AbstractUser
from .managers import UserManager


class User(AbstractUser):
    class Meta:
        db_table = 'auth_user'

    objects = UserManager()

    def __str__(self):
        return self.email


@receiver(post_save, sender=User)
def create_favorites(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
#    email = models.EmailField
    occupation = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='profile/img', blank=True, null=True)
    about = models.TextField(max_length=2000)
    profile_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    def __str__(self):
        return self.user.email

    def delete(self, *args, **kwargs):
        self.user.delete()
        return super(self.__class__, self).delete(*args, **kwargs)




'''class MyUser(AbstractUser):
    username = models.CharField(max_length=40, unique=True, db_index=True)
    email = models.EmailField(max_length=254, unique=True)
    is_email_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email'''


