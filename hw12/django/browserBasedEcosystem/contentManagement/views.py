from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET
# from django.contrib.auth.decorators import login_required
from application.decorators import auth_required
from django.contrib.auth import logout
from application.settings import LOGIN_URL

@require_GET
def welcome(request):
    user = request.user
    if user.is_authenticated:
        return render(request, 'controlPanel.html')
    return render(request, 'welcome.html')

@require_GET
@auth_required
def control_panel(request):
    return render(request, 'controlPanel.html')

@require_GET
@auth_required
def exit_account(request):
    logout(request)
    return redirect(LOGIN_URL)
