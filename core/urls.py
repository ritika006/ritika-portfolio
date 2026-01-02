from django.urls import path
from django_distill import distill_path
from .views import home

# Use a simple distill function that returns None for the homepage
def get_home():
    return None

urlpatterns = [
    distill_path('', home, name='home', distill_func=get_home),
]
