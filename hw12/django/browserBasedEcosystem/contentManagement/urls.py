from django.urls import path
from .views import control_panel, welcome, exit_account


urlpatterns = [
    path('', welcome, name='welcome'),
    path('controlPanel/', control_panel, name='control_panel'),
    path('logout/', exit_account, name='logout'),
]