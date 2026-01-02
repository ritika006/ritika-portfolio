from django.urls import path
from django_distill import distill_path
from .views import contact_view

def get_contact():
    return None

urlpatterns = [
    distill_path('', contact_view, name='contact', distill_func=get_contact),
]
