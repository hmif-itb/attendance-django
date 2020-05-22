from django.contrib import admin
from .models import Tenant, TenantStudent, KeyboardShortcut


class TenantAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_user_name', 'enabled')

    def get_user_name(self, obj):
        return obj.user.username

    get_user_name.short_description = 'Associated user'


admin.site.register(Tenant, TenantAdmin)


class TenantStudentAdmin(admin.ModelAdmin):
    list_display = ('nim', 'name', 'get_tenant_name')
    list_filter = ('tenant',)

    def get_tenant_name(self, obj):
        return obj.tenant.name

    get_tenant_name.short_description = 'Tenant name'


admin.site.register(TenantStudent, TenantStudentAdmin)


class KeyboardShortcutAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_tenant_name', 'key')
    list_filter = ('tenant',)

    def get_tenant_name(self, obj):
        return obj.tenant.name

    get_tenant_name.short_description = 'Tenant name'

admin.site.register(KeyboardShortcut, KeyboardShortcutAdmin)
