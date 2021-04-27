from django.contrib import admin
from .models import meeting, meetingMinutes, resource, event

# Register your models here.
admin.site.register(meeting)
admin.site.register(meetingMinutes)
admin.site.register(resource)
admin.site.register(event)
