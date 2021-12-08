from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET


@require_GET
def userControlPanelPageLoader(request):
    return render(request, 'userControlPanel.html')
