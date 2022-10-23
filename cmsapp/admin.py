from django.contrib import admin
from .models import Post
from .models import PostCategory


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class PostCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)

