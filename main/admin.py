# Register your models here.

from django.contrib import admin
from .models import Task, Login, Catalogue


admin.site.register(Task)
admin.site.register(Login)
# admin.site.register(Item)
admin.site.register(Catalogue)

