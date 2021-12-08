from django.shortcuts import get_object_or_404, render
import os
from django.urls.conf import path
from rest_framework import viewsets
from rest_framework.response import Response

from sharedClipboard.serializers import ClipboardFileSerializer, ClipboardFile

class SharedClipboardViewSet(viewsets.ModelViewSet):
    queryset = ClipboardFile.objects.all()
    serializer_class = ClipboardFileSerializer


