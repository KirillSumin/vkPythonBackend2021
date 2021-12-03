from django.shortcuts import render
from django.http import HttpResponse
import application.custom_exceptions as cExc
from django.views.decorators.http import require_GET

# Create your views here.\
@require_GET
def user_control_panel_page_loader(request):
    # try:
    #     if request.method != 'GET':
    #         raise cExc.HttpMethodIsNotSupported

        return render(request, 'userControlPanel.html')
    # except cExc.HttpMethodIsNotSupported:
    #     return HttpResponse(status=405)