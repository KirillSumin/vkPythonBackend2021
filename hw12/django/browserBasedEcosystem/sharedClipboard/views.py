import json
from rest_framework import viewsets
from rest_framework.response import Response
from sharedClipboard.serializers import ClipboardFileSerializer
from sharedClipboard.models import ClipboardFile
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from application.settings import EMAIL_HOST_USER, EMAIL_RECIPIENT_LIST

class SharedClipboardViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ClipboardFile.objects.all()
    serializer_class = ClipboardFileSerializer

    def list(self, request):
        queryset = ClipboardFile.objects.all().filter(owner=request.user)
        serializer = ClipboardFileSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            file = ClipboardFile.objects.get(pk=pk, owner=request.user)
            serializer = ClipboardFileSerializer(file)
            return Response(serializer.data)
        except ClipboardFile.DoesNotExist:
            return Response(
                {'error': 'file with this id does not exist or you dont have permission to get it'}, 
                status=404)
        except ValueError:
            return Response(
                {'error': 'incorrect value, only numbers support'}, 
                status=404)

    def create(self, request):
        serializer = ClipboardFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
        else:
            return Response(serializer.errors, status=400)
        user_str = str(request.user)
        send_mail(user_str + ' create new ClipboardFile', 
            'username: ' + user_str + '\n' + 'json: ' + json.dumps(serializer.validated_data), 
            EMAIL_HOST_USER, EMAIL_RECIPIENT_LIST, fail_silently=False)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            file = ClipboardFile.objects.get(pk=pk, owner=request.user)
            serializer = ClipboardFileSerializer(instance=file, data=request.data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=400)
            return Response(serializer.data)
        except ClipboardFile.DoesNotExist:
            return Response(
                {'error': 'file with this id does not exist or you dont have permission to get it'}, 
                status=404)
        except ValueError:
            return Response(
                {'error': 'incorrect value, only numbers support'}, 
                status=404)

    def destroy(self, request, pk=None):
        try:
            file = ClipboardFile.objects.get(pk=pk, owner=request.user)
            serializer = ClipboardFileSerializer(file)
            file.delete()
            return Response(serializer.data)
        except ClipboardFile.DoesNotExist:
            return Response(
                {'error': 'file with this id does not exist or you dont have permission to get it'}, 
                status=404)
        except ValueError:
            return Response(
                {'error': 'incorrect value, only numbers support'}, 
                status=404)
