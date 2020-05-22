from django.contrib import admin
from .models import Student, Attendance


class AttendanceAdmin(admin.ModelAdmin):
    fields = ['event', 'attendee']
    list_display = ('attendee', 'event', 'get_tenant_name', 'created_at')
    list_filter = ['event']

    def get_tenant_name(self, obj):
        return obj.event.tenant.name

    get_tenant_name.short_description = 'Tenant'


# Register your models here.
admin.site.register(Student)
admin.site.register(Attendance, AttendanceAdmin)