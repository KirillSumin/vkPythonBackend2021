from django.shortcuts import render
from django.http import HttpResponse
import application.custom_exceptions as cExc

# Create your views here.
def userControlPanelPageLoader(request):
    try:
        if request.method != 'GET':
            raise cExc.HttpMethodIsNotSupported

        return render(request, 'userControlPanel.html')
    except cExc.HttpMethodIsNotSupported:
        return HttpResponse(status=405)