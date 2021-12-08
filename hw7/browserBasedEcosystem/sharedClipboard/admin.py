from django.contrib import admin
from .models import ClipboardFile

class SharedClipboardAdmin(admin.ModelAdmin):
    list_filter = ('owner', 'type')
    list_display = ('path','create_data_time')

admin.site.register(ClipboardFile, SharedClipboardAdmin)

