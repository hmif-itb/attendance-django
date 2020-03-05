from django.contrib import admin
from .models import Attendee, Attendance

class AttendanceAdmin(admin.ModelAdmin):
    fields = ['event', 'attendee']
    list_display = ('attendee', 'event', 'created_at')
    list_filter = ['event']

# Register your models here.
admin.site.register(Attendee)
admin.site.register(Attendance, AttendanceAdmin)