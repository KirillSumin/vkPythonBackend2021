from django.urls import path
from .views import find_users_by_bio

urlpatterns = [
        path('find/<str:query>', find_users_by_bio),
]