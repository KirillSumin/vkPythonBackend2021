import os
from sharedClipboard.models import ClipboardFile
from rest_framework import serializers
from application.settings import BASE_DIR


USER_FILES_DIR = os.path.join(BASE_DIR, 'userFiles')

def file_exist_validator(data):
    if os.path.exists(os.path.join(USER_FILES_DIR, data['path'])):
            raise serializers.ValidationError('invalid path')

class ClipboardFileSerializer(serializers.ModelSerializer):
    # owner = serializers.PrimaryKeyRelatedField(label='Владелец файла', read_only=True)
    class Meta:
        model = ClipboardFile
        fields = ['id', 'path', 'type', 'create_data_time']
        validators = [file_exist_validator]



