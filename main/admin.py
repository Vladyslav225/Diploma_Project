# Register your models here.

from django.contrib import admin

from .models import Task, Catalogue


admin.site.register(Task)
admin.site.register(Catalogue)

