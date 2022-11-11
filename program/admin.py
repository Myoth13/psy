from django.contrib import admin
from .models import Program
from .models import ProgramCategory


class ProgramAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class ProgramCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


# Register your models here.
admin.site.register(Program, ProgramAdmin)
admin.site.register(ProgramCategory, ProgramCategoryAdmin)

