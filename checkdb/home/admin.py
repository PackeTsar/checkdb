from django.contrib import admin
from .models import Record


class RecordAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'address_family',
        'port',
        'protocol',
        'timestamp'
    ]


admin.site.register(Record, RecordAdmin)
