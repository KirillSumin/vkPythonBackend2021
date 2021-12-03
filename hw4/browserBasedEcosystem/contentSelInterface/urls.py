from django.urls import path
from .views import user_control_panel_page_loader

urlpatterns = [
    path('', user_control_panel_page_loader),
]