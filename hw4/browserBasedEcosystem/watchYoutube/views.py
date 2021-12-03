from django.shortcuts import render
from django.http import HttpResponse
import application.custom_exceptions as cExc
from django.views.decorators.http import require_GET

# Create your views here.
@require_GET
def sync_youtube_player_page_loader(request):
    # try:
    #     if request.method != 'GET':
    #         raise cExc.HttpMethodIsNotSupported

        return render(request, 'syncYoutubePlayer.html',
                      {"video_id": request.GET.get('v')})
    # except cExc.HttpMethodIsNotSupported:
    #     return HttpResponse(status=405)
