from django.urls import path
from .views import syncYoutubePlayerPageLoader

urlpatterns = [
    path('', syncYoutubePlayerPageLoader),
]