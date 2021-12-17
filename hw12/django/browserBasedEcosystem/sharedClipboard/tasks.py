from celery import shared_task
from django.core.mail import send_mail
from application.settings import EMAIL_HOST_USER, EMAIL_RECIPIENT_LIST
from sharedClipboard.models import ClipboardFile
import datetime

@shared_task
def email_num_of_files():
    time_now_str =  datetime.datetime.now().strftime("%Y-%m-%d-%H.%M.%S")
    num_files = str(len(ClipboardFile.objects.all()))
    send_mail('num of files, datetime: ' + time_now_str, 
           'number of files: ' + num_files +
           '\n' + time_now_str,
            EMAIL_HOST_USER, EMAIL_RECIPIENT_LIST, fail_silently=False)