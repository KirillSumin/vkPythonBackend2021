from django.urls import path
from .views import userControlPanelPageLoader

urlpatterns = [
    path('', userControlPanelPageLoader),
]