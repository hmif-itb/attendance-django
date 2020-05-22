from django.contrib import admin
from .models import Student, Attendance


class AttendanceAdmin(admin.ModelAdmin):
    fields = ['event', 'attendee']
    list_display = ('attendee', 'event', 'created_at')
    list_filter = ['event']


# Register your models here.
admin.site.register(Student)
admin.site.register(Attendance, AttendanceAdmin)