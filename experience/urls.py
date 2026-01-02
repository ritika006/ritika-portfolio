from django.urls import path
from django_distill import distill_path
from .views import experience_list

def get_experience():
    return None

urlpatterns = [
    distill_path('', experience_list, name='experience', distill_func=get_experience),
]
