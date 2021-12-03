from django.urls import path
from .views import new_file, file_info, list_files

urlpatterns = [
    path('newFile', new_file),
    path('listFiles', list_files),
    path('fileInfo', file_info),
]