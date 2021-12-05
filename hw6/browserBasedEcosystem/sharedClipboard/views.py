import json
import os
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from sharedClipboard.models import ClipboardFile
from users.models import User
from application.settings import BASE_DIR


USER_FILES_DIR = os.path.join(BASE_DIR, 'userFiles')

@csrf_exempt  # for postman normal working, REMOVE ON RELEASE
@require_POST
def create_clipboard_file(request, file_name = None):
    try:
        if file_name is None:
            return HttpResponse(status=400)

        json_data = json.loads(request.body)

        api_user = User.objects.get(username=json_data['username'])        # maybe use get_object_or_404 ?
        api_user_path = os.path.join(USER_FILES_DIR, api_user.username)
        api_user_path_file = os.path.join(api_user_path, file_name)

        if not os.path.exists(api_user_path):
            os.mkdir(api_user_path)   

        if os.path.exists(api_user_path_file):
            return HttpResponse(status=400)

        with open(api_user_path_file, 'w+') as file_handler:
             pass

        file_type = ''
        first_point_index = file_name.find('.')
        if first_point_index != -1:
            file_type = file_name[first_point_index + 1:]

        ClipboardFile.objects.create(path=os.path.join(api_user.username, file_name), owner=api_user,
        type=file_type)
    
        return JsonResponse({'error': 'no', 'username': json_data['username'], 
        'path': os.path.join(api_user.username, file_name), 'type': file_type})

    except (User.DoesNotExist, OSError):
        return HttpResponse(status=400)
    except json.decoder.JSONDecodeError:
        # return JsonResponse({'error': 'json invalid format'})
        return HttpResponse(status=400)
    except KeyError:
        # return JsonResponse({'error': 'incorrect set of keys'})
        return HttpResponse(status=400)

@csrf_exempt  # for postman normal working, REMOVE ON RELEASE
@require_GET
def read_clipboard_file(request, file_name = None):
    try:
        if file_name is None:
            return HttpResponse(status=400)

        json_data = json.loads(request.body)

        api_user = User.objects.get(username=json_data['username'])       # maybe use get_object_or_404 ?

        api_user_file_obj = ClipboardFile.objects.get(owner = api_user,   # maybe use get_object_or_404 ?
        path=os.path.join(api_user.username, file_name))

        return JsonResponse({'error': 'no', 'username': json_data['username'], 
        'path': api_user_file_obj.path, 'type': api_user_file_obj.type})

    except (ClipboardFile.DoesNotExist, User.DoesNotExist, OSError):
        return HttpResponse(status=404)
    except json.decoder.JSONDecodeError:
        # return JsonResponse({'error': 'json invalid format'})
        return HttpResponse(status=400)
    except KeyError:
        # return JsonResponse({'error': 'incorrect set of keys'})
        return HttpResponse(status=400)


@csrf_exempt  # for postman normal working, REMOVE ON RELEASE
@require_GET
def read_list_of_clipboard_files(request):
    try:
        json_data = json.loads(request.body)

        api_user = User.objects.get(username=json_data['username'])       # maybe use get_object_or_404 ?

        api_user_all_file_objects = ClipboardFile.objects.all().filter(owner = api_user)

        api_user_all_file_objects_info = []
        for api_user_file_obj in api_user_all_file_objects:
            api_user_all_file_objects_info.append({'path': api_user_file_obj.path, 'type': api_user_file_obj.type})

        return JsonResponse({'error': 'no', 'list_files': api_user_all_file_objects_info})

    except (ClipboardFile.DoesNotExist, User.DoesNotExist, OSError):
        return HttpResponse(status=404)
    except json.decoder.JSONDecodeError:
        # return JsonResponse({'error': 'json invalid format'})
        return HttpResponse(status=400)
    except KeyError:
        # return JsonResponse({'error': 'incorrect set of keys'})
        return HttpResponse(status=400)

@csrf_exempt  # for postman normal working, REMOVE ON RELEASE
@require_http_methods(['PUT'])
def update_clipboard_file(request, old_file_name = None):
    try:
        if old_file_name is None:
            return HttpResponse(status=400)

        json_data = json.loads(request.body)
        new_file_name = json_data['new_name']

        api_user = User.objects.get(username=json_data['username'])  # maybe use get_object_or_404 ?
        api_user_path = os.path.join(USER_FILES_DIR, api_user.username)
        api_user_new_path_file = os.path.join(api_user_path, new_file_name)  

        if os.path.exists(api_user_new_path_file):
            return HttpResponse(status=400)

        api_user_old_file_obj = ClipboardFile.objects.get(owner = api_user,   # maybe use get_object_or_404 ?
        path=os.path.join(api_user.username, old_file_name))
        
        new_file_type = ''
        first_point_index = new_file_name.find('.')
        if first_point_index != -1:
            new_file_type = new_file_name[first_point_index + 1:]

        api_user_old_file_obj.path = os.path.join(api_user.username, new_file_name)
        api_user_old_file_obj.type = new_file_type
        api_user_old_file_obj.save(update_fields=["path", "type"])

        os.rename(os.path.join(api_user_path, old_file_name), os.path.join(api_user_path, new_file_name))

        return JsonResponse({'error': 'no', 'username': json_data['username'], 
        'path': api_user_old_file_obj.path, 'type': api_user_old_file_obj.type})

    except (ClipboardFile.DoesNotExist, User.DoesNotExist, OSError):
        return HttpResponse(status=404)
    except json.decoder.JSONDecodeError:
        # return JsonResponse({'error': 'json invalid format'})
        return HttpResponse(status=400)
    except KeyError:
        # return JsonResponse({'error': 'incorrect set of keys'})
        return HttpResponse(status=400)

@csrf_exempt  # for postman normal working, REMOVE ON RELEASE
@require_http_methods(['DELETE'])
def delete_clipboard_file(request, file_name = None):
    try:
        if file_name is None:
            return HttpResponse(status=400)

        json_data = json.loads(request.body)

        api_user = User.objects.get(username=json_data['username'])       # maybe use get_object_or_404 ?       
        api_user_path = os.path.join(USER_FILES_DIR, api_user.username)
        
        api_user_file_obj = ClipboardFile.objects.get(owner = api_user,   # maybe use get_object_or_404 ?
        path=os.path.join(api_user.username, file_name))

        os.remove(os.path.join(api_user_path, file_name))

        api_user_file_obj_info = {'error':'no', 'username': json_data['username'], 
        'path': api_user_file_obj.path, 'type': api_user_file_obj.type}
        
        api_user_file_obj.delete()

        return JsonResponse(api_user_file_obj_info)

    except (ClipboardFile.DoesNotExist, User.DoesNotExist, OSError):
        return HttpResponse(status=404)
    except json.decoder.JSONDecodeError:
        # return JsonResponse({'error': 'json invalid format'})
        return HttpResponse(status=400)
    except KeyError:
        # return JsonResponse({'error': 'incorrect set of keys'})
        return HttpResponse(status=400)