from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    fields = ['tenant', 'name', 'date', 'code', 'checkin_open']
    readonly_fields = ['code']
    list_display = ('name', 'code', 'get_tenant_name', 'checkin_open')
    list_filter = ('tenant', 'checkin_open')

    def get_tenant_name(self, obj):
        return obj.tenant.name

    get_tenant_name.short_description = "Tenant name"

    def regenerate_code(modeladmin, request, queryset):
        for obj in queryset:
            obj.regenerate_code()

    regenerate_code.short_description = "Regenerate code"

    actions = [regenerate_code]

admin.site.register(Event, EventAdmin)