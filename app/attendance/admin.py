from django.contrib import admin
from .models import Attendee, Attendance, AttendeeMajor, AttendeeYear

class AttendanceAdmin(admin.ModelAdmin):
    fields = ['event', 'attendee']
    list_display = ('attendee', 'event', 'created_at')
    list_filter = ['event']

class AttendeeMajorAdmin(admin.ModelAdmin):
    fields = ['name', 'nim_prefix', 'keyboard_shortcut']
    list_display = ('name', 'nim_prefix', 'keyboard_shortcut')

class AttendeeYearAdmin(admin.ModelAdmin):
    fields = ['name', 'nim_prefix', 'keyboard_shortcut']
    list_display = ('name', 'nim_prefix', 'keyboard_shortcut')

# Register your models here.
admin.site.register(Attendee)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(AttendeeMajor, AttendeeMajorAdmin)
admin.site.register(AttendeeYear, AttendeeYearAdmin)