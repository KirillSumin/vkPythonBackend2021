from django.shortcuts import redirect
from application.settings import LOGIN_URL

def auth_required(func):
    def wrapper(request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            return func(request, *args, **kwargs)
        else:
            return redirect(LOGIN_URL)
    return wrapper