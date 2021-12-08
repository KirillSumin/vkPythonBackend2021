import os
from sharedClipboard.models import ClipboardFile
from rest_framework import serializers
from application.settings import BASE_DIR


USER_FILES_DIR = os.path.join(BASE_DIR, 'userFiles')

def file_exist_validator(data):
     if os.path.exists(os.path.join(USER_FILES_DIR, data['path'])):
            raise serializers.ValidationError('invalid path')

class ClipboardFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClipboardFile
        fields = '__all__'
        validators = [file_exist_validator]
