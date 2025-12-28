# Register your models here.

from django.contrib import admin
from .models import Project, Technology

admin.site.register(Project)
admin.site.register(Technology)

