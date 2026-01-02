from django.urls import path
from django_distill import distill_path
from .views import project_list, project_detail
from .models import Project

def get_projects():
    return None

def get_project_slugs():
    return (dict(slug=project.slug) for project in Project.objects.all())

urlpatterns = [
    distill_path('', project_list, name='project_list', distill_func=get_projects),
    distill_path('<slug:slug>/', project_detail, name='project_detail', distill_func=get_project_slugs),
]
