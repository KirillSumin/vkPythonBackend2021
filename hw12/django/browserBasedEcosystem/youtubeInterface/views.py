from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
# from django.contrib.auth.decorators import login_required
from application.decorators import auth_required

@csrf_exempt  # for postman normal working, REMOVE ON RELEASE
@require_GET
@auth_required
def sync_youtube(request):
        return render(request, 'syncYoutube.html',
                      {"video_id": request.GET.get('v')})
