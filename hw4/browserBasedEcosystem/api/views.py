from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import application.custom_exceptions as cExc
from django.views.decorators.http import require_GET, require_POST

files = []


# Create your views here.
@csrf_exempt
@require_POST
def new_file(request):
    try:
        # if request.method != 'POST':
        #     raise cExc.HttpMethodIsNotSupported

        json_data = json.loads(request.body)

        file_exist = False
        for file in files:
            if file['id'] == json_data['id']:
                file_exist = True

        if file_exist:
            raise cExc.FileIdAlreadyExist

        files.append({"id": json_data['id'],
                      "name": json_data['name'],
                      "type": json_data['type'],
                      "description": json_data['description']})

        return JsonResponse({'error': 'no'})
    # except cExc.HttpMethodIsNotSupported:
    #     # return HttpResponse(status=405)  # raise ...
    #     return JsonResponse({'error': 'method is not supported'})
    except json.decoder.JSONDecodeError:
        return JsonResponse({'error': 'json invalid format'})
    except cExc.FileIdAlreadyExist:
        return JsonResponse({'error': 'change id, file already exist'})
    except KeyError:
        return JsonResponse({'error': 'incorrect set of keys'})

@csrf_exempt
@require_GET
def list_files(request):
    try:
        # if request.method != 'GET':
        #     raise cExc.HttpMethodIsNotSupported

        files_base_info = []
        for file in files:
            files_base_info.append({'id': file['id'], 'name': file['name']})

        return JsonResponse({'error': 'no',
                             'listFiles': files_base_info
                             })
    # except cExc.HttpMethodIsNotSupported:
    #     return JsonResponse({'error': 'method is not supported',
    #                          'listFiles': []
    #                          })
    except KeyError:
        return JsonResponse({'error': 'internal error',
                             'listFiles': []})

@csrf_exempt
@require_POST
def file_info(request):
    try:
        # if request.method != 'GET':
        #     raise cExc.HttpMethodIsNotSupported

        json_data = json.loads(request.body)

        files_full_info = None
        for file in files:
            if file['id'] == json_data['id']:
                files_full_info = file
        if files_full_info is None:
            raise cExc.FileNotExist

        return JsonResponse({'error': 'no',
                             'fileInfo': files_full_info})
    # except cExc.HttpMethodIsNotSupported:
    #     return JsonResponse({'error': 'method is not supported',
    #                          'fileInfo': {}
    #                          })
    except json.decoder.JSONDecodeError:
        return JsonResponse({'error': 'json invalid format',
                             'fileInfo': {}})
    except cExc.FileNotExist:
        return JsonResponse({'error': 'file with the received id does not exist',
                             'fileInfo': {}})
    except KeyError:
        return JsonResponse({'error': 'internal error',
                             'fileInfo': {}})
