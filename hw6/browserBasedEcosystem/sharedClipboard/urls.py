from django.urls import path
from .views import create_clipboard_file, read_clipboard_file, read_list_of_clipboard_files, update_clipboard_file, delete_clipboard_file

urlpatterns = [
    path('create/<str:file_name>', create_clipboard_file),
    path('read/<str:file_name>', read_clipboard_file),
    path('read', read_list_of_clipboard_files),
    path('update/<str:old_file_name>', update_clipboard_file),
    path('delete/<str:file_name>', delete_clipboard_file),
]