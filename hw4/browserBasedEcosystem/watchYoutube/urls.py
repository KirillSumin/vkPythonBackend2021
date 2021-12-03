from django.urls import path
from .views import sync_youtube_player_page_loader

urlpatterns = [
    path('', sync_youtube_player_page_loader),
]