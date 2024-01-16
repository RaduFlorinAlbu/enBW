from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    def bucket_name(self, obj):
        return obj.bucket.name or "-"
    list_display = ["id", "uuid", "title", "bucket_name"]

admin.site.register(Event, EventAdmin)