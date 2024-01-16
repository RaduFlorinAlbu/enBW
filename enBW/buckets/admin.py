from django.contrib import admin
from buckets.models import Bucket
from events.models import Event
from buckets.forms import BucketForm

class EventInLine(admin.TabularInline):
    model = Event
    extra = 1
class BucketAdmin(admin.ModelAdmin):
    form = BucketForm
    inlines = [EventInLine]
    def display_events(self,obj):
        events_from_my_bucket = obj.events.all()
        return ", ".join(event.title for event in events_from_my_bucket)

    list_display = ["id", "name","display_events"]


admin.site.register(Bucket, BucketAdmin)