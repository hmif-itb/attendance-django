from django.contrib import admin
from .models import EventCategory, Event

class EventAdmin(admin.ModelAdmin):
    fields = ['name', 'date', 'category', 'code', 'checkin_open']
    readonly_fields = ['code']
    list_display = ('name', 'code', 'category')

    def regenerate_code(modeladmin, request, queryset):
        for obj in queryset:
            obj.regenerate_code()

    regenerate_code.short_description = "Regenerate code"

    actions = [regenerate_code]

admin.site.register(EventCategory)
admin.site.register(Event, EventAdmin)