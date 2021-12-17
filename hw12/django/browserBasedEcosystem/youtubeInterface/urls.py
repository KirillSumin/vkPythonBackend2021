from django.urls import path
from .views import sync_youtube

urlpatterns = [
    path('', sync_youtube),
]