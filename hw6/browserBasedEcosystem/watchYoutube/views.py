from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_POST

@csrf_exempt  # for postman normal working, REMOVE ON RELEASE
@require_GET
def syncYoutubePlayerPageLoader(request):
        return render(request, 'syncYoutubePlayer.html',
                      {"video_id": request.GET.get('v')})
